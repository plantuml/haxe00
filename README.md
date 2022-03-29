# PlantUML 2

For the next major version, PlantUML will be developped using [Haxe language](https://haxe.org).

Moving to [Haxe](https://haxe.org/documentation/introduction/compiler-targets.html) means that we will have a native implementation of PlantUML in all following languages:
* Javascript
* Java (JVM)
* Python 3
* PHP7
* C#
* C++

This way, PlantUML language could be available everywhere.


# Current situation

PlantUML 2 is really a rewrite of the existing Java code.

Haxe provides everything (and more!) that we need for PlantUML (oriented-object, regular expression, nice standard library), however re-implementing all that PlantUML is currently doing will takes time (that is, at least 2 years).

This means that we are going to slow down on adding new features in current PlantUML 1. We will only focus on bug fixes.

Current version of PlantUML 2 provides only a **tiny** part of what PlantUML 1 is capable of:
* only Mindmap diagrams
* only SVG output
* no preprocessor
* no standard library

Next step is now to add Sequence Diagram.


## How to build it

You first have to install [Haxe 4](https://haxe.org).

The two following libraries are used:

```
haxelib install utest
haxelib install haxe-strings
```

If you have some HTTPS certificate issues (because of proxy for example), you can use:

```
haxelib install utest -R http://lib.haxe.org/
haxelib install haxe-strings -R http://lib.haxe.org/
```

For building, you have to launch the `haxe` command with some `.hxml` build file.

### Unit testing

```
haxe unit-test.hxml 
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


# Building

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
