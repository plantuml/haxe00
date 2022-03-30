#!/bin/bash
export PATH=/opt/jdk1.8.0_102/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/Arnaud.Roques/n/bin:/home/Arnaud.Roques
export JAVA_HOME=/opt/jdk1.8.0_102
rm *.out unit-test.py
haxe unit-test.hxml
python3 unit-test.py > unit-test-py.out
java -jar unit-test-java/MainTest.jar > unit-test-java.out
cat *.out
grep results unit-test-py.out
grep results unit-test-java.out
