#!/usr/bin/python3
import tarfile
import sys
import io
import time

tarname, version = sys.argv[1:]

tardata = sys.stdin.read()
tarstream = io.BytesIO(tardata)

verstream = io.StringIO(version + "\n")
verinfo = tarfile.TarInfo("%sVERSION" % tarname)
verinfo.mode = 0o664
verinfo.size = len(verstream.getvalue())
verinfo.mtime = time.time()

tar = tarfile.TarFile(mode='a', fileobj=tarstream)
tar.addfile(verinfo, verstream)
tar.close()

sys.stdout.write(tarstream.getvalue())
