#!/bin/bash
export PATH=/opt/jdk1.8.0_102/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/Arnaud.Roques/n/bin:/home/Arnaud.Roques
export JAVA_HOME=/opt/jdk1.8.0_102
haxe test-full.hxml
java -jar TestJvm/MainTest.jar
