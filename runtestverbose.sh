#!/bin/bash
export PATH=/opt/jdk1.8.0_102/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/Arnaud.Roques/n/bin:/home/Arnaud.Roques
export JAVA_HOME=/opt/jdk1.8.0_102
rm *.py *.tmp
haxe test-full.hxml
python3 TestPy.py > TestPy.tmp
java -jar TestJvm/MainTest-Debug.jar > TestJvm.tmp
cat *.tmp
grep results TestPy.tmp
grep results TestJvm.tmp
haxe js.hxml
