:hello
del *.py
haxe test-full.hxml
python TestPy.py
java -jar TestJvm/MainTest-Debug.jar
pause
goto hello
