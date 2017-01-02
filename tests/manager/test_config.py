# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from unittest import TestCase
from collections import defaultdict

from nose.tools import raises

from tests.helper.stubs import Core, admin_user, normal_user

from pyload.api import InvalidConfigSection
from pyload.database import DatabaseBackend
from pyload.config.parser import ConfigParser
from pyload.manager.config import ConfigManager
from pyload.utils import primary_uid

admin_user  = primary_uid(admin_user)
normal_user = primary_uid(normal_user)


class TestConfigManager(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.core = Core()
        cls.db = DatabaseBackend(cls.core)
        cls.core.db = cls.db
        cls.db.manager = cls.core
        cls.db.manager.status_msg = defaultdict(lambda: "statusmsg")
        cls.parser = ConfigParser()
        cls.config = ConfigManager(cls.core, cls.parser)
        cls.db.setup()

    def setUp(self):
        self.db.clear_all_configs()
        # used by some tests, needs to be deleted
        self.config.delete("plugin", admin_user)


    def addConfig(self):
        self.config.add_config_section("plugin", "Name", "desc", "something",
            [("value", "str", "label", "default")])

    def test_db(self):

        self.db.save_config("plugin", "some value", 0)
        self.db.save_config("plugin", "some other value", 1)

        assert self.db.load_config("plugin", 0) == "some value"
        assert self.db.load_config("plugin", 1) == "some other value"

        d = self.db.load_all_configs()
        assert d[0]['plugin'] == "some value"
        assert self.db.load_configs_for_user(0)['plugin'] == "some value"

        self.db.delete_config("plugin", 0)

        assert 0 not in self.db.load_all_configs()
        assert "plugin" not in self.db.load_configs_for_user(0)

        self.db.delete_config("plugin")

        assert not self.db.load_all_configs()
        assert self.db.load_config("plugin") == ""

    def test_parser(self):
        assert self.config.get("general", "language")
        self.config['general']['language'] = "de"
        assert self.config['general']['language'] == "de"
        assert self.config.get("general", "language", admin_user) == "de"

    def test_user(self):
        self.add_config()

        assert self.config['plugin']['value'] == "default"
        assert self.config.get("plugin", "value", admin_user) == "default"
        assert self.config.get("plugin", "value", normal_user) == "default"

        assert self.config.set("plugin", "value", False, user=normal_user)
        assert self.config.get("plugin", "value", normal_user) is False
        assert self.config['plugin']['value'] == "default"

        assert self.config.set("plugin", "value", True, user=admin_user)
        assert self.config.get("plugin", "value", admin_user) is True
        assert self.config['plugin']['value'] is True
        assert self.config.get("plugin", "value", normal_user) is False

        self.config.delete("plugin", normal_user)
        assert self.config.get("plugin", "value", normal_user) == "default"

        self.config.delete("plugin")
        assert self.config.get("plugin", "value", admin_user) == "default"
        assert self.config['plugin']['value'] == "default"

        # should not trigger something
        self.config.delete("foo")

    def test_sections(self):
        self.add_config()

        i = 0
        # there should be only one section, with no values
        for name, config, values in self.config.iter_sections(admin_user):
            assert name == "plugin"
            assert values == {}
            i +=1
        assert i == 1

        assert self.config.set("plugin", "value", True, user=admin_user)

        i = 0
        # now we assert the correct values
        for name, config, values in self.config.iter_sections(admin_user):
            assert name == "plugin"
            assert values == {"value":True}
            i +=1
        assert i == 1

    def test_get_section(self):
        self.add_config()
        self.assertEqual(self.config.get_section("plugin")[0].label, "Name")

    # TODO: more save tests are needed
    def test_saveValues(self):
        self.add_config()
        self.config.save_values(admin_user, "plugin")

    @raises(InvalidConfigSection)
    def test_restricted_access(self):
        self.config.get("general", "language", normal_user)

    @raises(InvalidConfigSection)
    def test_error(self):
        self.config.get("foo", "bar")

    @raises(InvalidConfigSection)
    def test_error_set(self):
        self.config.set("foo", "bar", True)
