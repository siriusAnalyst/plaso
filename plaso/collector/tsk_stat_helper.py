#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2012 The Plaso Project Authors.
# Please see the AUTHORS file for details on individual authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The SleuthKit stat helper functions."""

from plaso.lib import pfile


def GetTskDirectoryStat(directory_object):
  """Return a stat object for a TSK directory object.

  Args:
    directory_object: A pyts3k.Directory object.

  Returns:
    A pfile.Stats object for the directory.
  """
  stat = pfile.Stats()

  info = getattr(directory_object, 'info', None)
  if not info:
    return stat

  try:
    meta = info.fs_file.meta
  except AttributeError:
    return stat

  if not meta:
    return stat

  fs_type = ''
  stat.mode = getattr(meta, 'mode', None)
  stat.ino = getattr(meta, 'addr', None)
  stat.nlink = getattr(meta, 'nlink', None)
  stat.uid = getattr(meta, 'uid', None)
  stat.gid = getattr(meta, 'gid', None)
  stat.size = getattr(meta, 'size', None)
  stat.atime = getattr(meta, 'atime', None)
  stat.atime_nano = getattr(meta, 'atime_nano', None)
  stat.crtime = getattr(meta, 'crtime', None)
  stat.crtime_nano = getattr(meta, 'crtime_nano', None)
  stat.mtime = getattr(meta, 'mtime', None)
  stat.mtime_nano = getattr(meta, 'mtime_nano', None)
  stat.ctime = getattr(meta, 'ctime', None)
  stat.ctime_nano = getattr(meta, 'ctime_nano', None)
  stat.dtime = getattr(meta, 'dtime', None)
  stat.dtime_nano = getattr(meta, 'dtime_nano', None)
  stat.bkup_time = getattr(meta, 'bktime', None)
  stat.bkup_time_nano = getattr(meta, 'bktime_nano', None)
  fs_type = str(info.fs_info.ftype)

  if fs_type.startswith('TSK_FS_TYPE'):
    stat.fs_type = fs_type[12:]
  else:
    stat.fs_type = fs_type

  return stat
