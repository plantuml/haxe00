package com.plantuml.command.regex;

abstract class AbstractRegex implements IRegex {
	private final patternString:String;

	public function getPatternString():String {
		return patternString;
	}

	public function new(s:String) {
		this.patternString = s;
	}

	public function match(full:String):Bool {
		var r = new EReg(patternString, "i");
		return r.match(full);
	}

	public function matchArray(full:String):Array<String> {
		var r = new EReg(patternString, "i");
		if (r.match(full) == false)
			return null;

		var result = [];
		var i = 1;
		try {
			while (true) {
				result.push(r.matched(i));
				i = i + 1;
			}
		} catch (e:haxe.Exception) {
			return result;
		}
	}
}
