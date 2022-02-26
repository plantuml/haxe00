# Haxe project

This is a Proof Of Concept to build a PlantUML implementation on Haxe.

This would allow to run PlantUML natively in Java, Python and JavaScript.

Don't expect to use it on yours projects. Currently, only a **tiny** part of PlantUML has been translated.

You can just use mindmap diagrams:

```
@startminmap
* WORLD
** America
*** Canada
*** USA
** Europe
*** UK
*** France
*** Germany
*** Italy
** Africa
@endmindmap
```

## How to build it

You will need [Haxe 4.2.4](https://haxe.org) to build it.

The two following libraries are used:

```
haxelib install utest
haxelib haxe-strings
```

Then build the JavaScript version:
```
haxe js.hxml 
```

Or the Command Line Interface (Java & Python):
```
haxe CLI.hxml 
```


After the build, you can run the python command line:
```
python3 Main.py foo.puml foo.hxml
```

Or the java one:
```
java -jar jvm/Main.jar foo.puml foo.hxml
```

Or open the html page **main.html**.

