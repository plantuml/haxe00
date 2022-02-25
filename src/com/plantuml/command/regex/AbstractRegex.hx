package com.plantuml.command.regex;

abstract class AbstractRegex implements IRegex {
	var pattern:String;

	public function getPattern():String {
		return pattern;
	}

	public function match(full:String):Bool {
		var r = new EReg(pattern, "i");
		return r.match(full);
	}

	public function matchArray(full:String):Array<String> {
		var r = new EReg(pattern, "i");
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
