#!/bin/bash
export PATH=/opt/jdk1.8.0_102/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/Arnaud.Roques/n/bin:/home/Arnaud.Roques
export JAVA_HOME=/opt/jdk1.8.0_102
rm *.out unit-test.py
haxe unit-test.hxml
python3 unit-test.py > unit-test-py.out
java -jar unit-test/MainTest.jar > unit-test-java.out
#cat *.out

if grep "ALL TESTS OK" unit-test-py.out; then
echo "ok python"
else
cat unit-test-py.out
fi
if grep "ALL TESTS OK" unit-test-java.out; then
echo "ok java"
else
cat unit-test-java.out
fi

grep results *.out
