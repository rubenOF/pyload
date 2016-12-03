#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autogenerated by pyload
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

from __future__ import absolute_import
from .apitypes import *

enums = [
    "Connection",
    "DownloadState",
    "DownloadStatus",
    "FileStatus",
    "InputType",
    "Interaction",
    "MediaType",
    "PackageStatus",
    "Permission",
    "ProgressType",
    "Role",
]

classes = {
    'AccountInfo': [int, basestring, basestring, int, bool, int, int, int, bool, bool, bool, (list, ConfigItem)],
    'AddonInfo': [basestring, basestring, basestring],
    'AddonService': [basestring, basestring, basestring, (list, basestring), bool, int],
    'ConfigHolder': [basestring, basestring, basestring, basestring, (list, ConfigItem), (None, (list, AddonInfo))],
    'ConfigInfo': [basestring, basestring, basestring, basestring, bool, (None, bool)],
    'ConfigItem': [basestring, basestring, basestring, Input, basestring],
    'DownloadInfo': [basestring, basestring, basestring, int, basestring, basestring],
    'DownloadProgress': [int, int, int, int, int],
    'EventInfo': [basestring, (list, basestring)],
    'FileDoesNotExist': [int],
    'FileInfo': [int, basestring, int, int, int, int, int, int, int, (None, DownloadInfo)],
    'Input': [int, (None, basestring), (None, basestring)],
    'InteractionTask': [int, int, Input, basestring, basestring, basestring],
    'InvalidConfigSection': [basestring],
    'LinkStatus': [basestring, basestring, int, int, (None, basestring), (None, basestring)],
    'OnlineCheck': [int, (dict, basestring, LinkStatus)],
    'PackageDoesNotExist': [int],
    'PackageInfo': [int, basestring, basestring, int, int, basestring, basestring, basestring, int, (list, basestring), int, bool, int, PackageStats, (list, int), (list, int)],
    'PackageStats': [int, int, int, int],
    'ProgressInfo': [basestring, basestring, basestring, int, int, int, int, int, (None, DownloadProgress)],
    'ServiceDoesNotExist': [basestring, basestring],
    'ServiceException': [basestring],
    'StatusInfo': [int, int, int, int, int, bool, bool, bool, bool, int],
    'TreeCollection': [PackageInfo, (dict, int, FileInfo), (dict, int, PackageInfo)],
    'UserData': [int, basestring, basestring, int, int, basestring, int, int, basestring, int, int, basestring],
    'UserDoesNotExist': [basestring],
}

methods = {
    'addLinks': None,
    'addLocalFile': None,
    'addPackage': int,
    'addPackageChild': int,
    'addPackageP': int,
    'addUser': UserData,
    'checkContainer': OnlineCheck,
    'checkHTML': OnlineCheck,
    'checkLinks': OnlineCheck,
    'createAccount': AccountInfo,
    'createPackage': int,
    'deleteConfig': None,
    'deleteFiles': bool,
    'deletePackages': bool,
    'findFiles': TreeCollection,
    'findPackages': TreeCollection,
    'freeSpace': int,
    'generateDownloadLink': basestring,
    'generatePackages': (dict, basestring, list),
    'getAccountInfo': AccountInfo,
    'getAccountTypes': (list, basestring),
    'getAccounts': (list, AccountInfo),
    'getAddonHandler': (dict, basestring, list),
    'getAllFiles': TreeCollection,
    'getAllInfo': (dict, basestring, list),
    'getAllUserData': (dict, int, UserData),
    'getAvailablePlugins': (list, ConfigInfo),
    'getConfig': (dict, basestring, ConfigHolder),
    'getConfigValue': basestring,
    'getCoreConfig': (list, ConfigInfo),
    'getFileInfo': FileInfo,
    'getFileTree': TreeCollection,
    'getFilteredFileTree': TreeCollection,
    'getFilteredFiles': TreeCollection,
    'getInfoByPlugin': (list, AddonInfo),
    'getInteractionTasks': (list, InteractionTask),
    'getLog': (list, basestring),
    'getPackageContent': TreeCollection,
    'getPackageInfo': PackageInfo,
    'getPluginConfig': (list, ConfigInfo),
    'getProgressInfo': (list, ProgressInfo),
    'getQuota': int,
    'getServerVersion': basestring,
    'getStatusInfo': StatusInfo,
    'getUserData': UserData,
    'getWSAddress': basestring,
    'invokeAddon': basestring,
    'invokeAddonHandler': basestring,
    'isInteractionWaiting': bool,
    'loadConfig': ConfigHolder,
    'login': bool,
    'moveFiles': bool,
    'movePackage': bool,
    'orderFiles': None,
    'orderPackage': None,
    'parseLinks': (dict, basestring, list),
    'pauseServer': None,
    'pollResults': OnlineCheck,
    'quit': None,
    'recheckPackage': None,
    'removeAccount': None,
    'removeFiles': None,
    'removePackages': None,
    'removeUser': None,
    'restart': None,
    'restartFailed': None,
    'restartFile': None,
    'restartPackage': None,
    'saveConfig': None,
    'searchSuggestions': (list, basestring),
    'setConfigValue': None,
    'setInteractionResult': None,
    'setPackagePaused': int,
    'setPassword': bool,
    'stopAllDownloads': None,
    'stopDownloads': None,
    'togglePause': bool,
    'toggleReconnect': bool,
    'unpauseServer': None,
    'updateAccount': AccountInfo,
    'updateAccountInfo': None,
    'updatePackage': PackageInfo,
    'updateUserData': None,
    'uploadContainer': int,
}