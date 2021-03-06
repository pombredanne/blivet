#!/usr/bin/python
import unittest

import blivet.formats.fs as fs

from . import fstesting

class Ext2FSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.Ext2FS
    _resizable = True

class Ext3FSTestCase(Ext2FSTestCase):
    _fs_class = fs.Ext3FS

class Ext4FSTestCase(Ext3FSTestCase):
    _fs_class = fs.Ext4FS

class FATFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.FATFS
    _resizable = False

class EFIFSTestCase(FATFSTestCase):
    _fs_class = fs.EFIFS

class BTRFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.BTRFS
    _resizable = False

@unittest.skip("Unable to create GFS2 filesystem.")
class GFS2TestCase(fstesting.FSAsRoot):
    _fs_class = fs.GFS2
    _resizable = False

class JFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.JFS
    _resizable = False

class ReiserFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.ReiserFS
    _resizable = False

class XFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.XFS
    _resizable = False

class HFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.HFS
    _resizable = False

class AppleBootstrapFSTestCase(HFSTestCase):
    _fs_class = fs.AppleBootstrapFS

class HFSPlusTestCase(fstesting.FSAsRoot):
    _fs_class = fs.HFSPlus
    _resizable = False

class MacEFIFSTestCase(HFSPlusTestCase):
    _fs_class = fs.MacEFIFS

@unittest.skip("Unable to create because NTFS._formattable is False.")
class NTFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.NTFS
    _resizable = True

@unittest.skip("Unable to create because device fails deviceCheck().")
class NFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.NFS
    _resizable = False

class NFSv4TestCase(NFSTestCase):
    _fs_class = fs.NFSv4

class Iso9660FS(fstesting.FSAsRoot):
    _fs_class = fs.Iso9660FS
    _resizable = False

@unittest.skip("Too strange to test using this framework.")
class NoDevFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.NoDevFS
    _resizable = False

class DevPtsFSTestCase(NoDevFSTestCase):
    _fs_class = fs.DevPtsFS

class ProcFSTestCase(NoDevFSTestCase):
    _fs_class = fs.ProcFS

class SysFSTestCase(NoDevFSTestCase):
    _fs_class = fs.SysFS

class TmpFSTestCase(NoDevFSTestCase):
    _fs_class = fs.TmpFS

class SELinuxFSTestCase(NoDevFSTestCase):
    _fs_class = fs.SELinuxFS

class USBFSTestCase(NoDevFSTestCase):
    _fs_class = fs.USBFS

class BindFSTestCase(fstesting.FSAsRoot):
    _fs_class = fs.BindFS
    _resizable = False

if __name__ == "__main__":
    unittest.main()
