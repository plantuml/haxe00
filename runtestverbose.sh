#!/bin/bash
export PATH=/opt/jdk1.8.0_102/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/Arnaud.Roques/n/bin:/home/Arnaud.Roques
export JAVA_HOME=/opt/jdk1.8.0_102
rm *.py *.tmp
haxe unit-test.hxml
python3 unit-test.py > unit-test-py.tmp
java -jar unit-test-java/MainTest.jar > unit-test-java.tmp
cat *.tmp
grep results unit-test-py.tmp
grep results unit-test-java.tmp
