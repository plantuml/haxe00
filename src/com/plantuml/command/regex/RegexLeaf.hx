package com.plantuml.command.regex;

class RegexLeaf extends AbstractRegex implements IRegex {
	private final name:String;
	private final size:Int;

	public function getSize():Int {
		return size;
	}

	public function new(size:Int, pattern:String, ?name:String) {
		this.name = name;
		super(pattern);
		this.size = size;
	}

	function toString():String {
		return name + "=" + getPatternString();
	}

	public function eat(array:Array<String>, map:Map<String, String>):Void {
		if (size == 1) {
			final s = array.pop();
			if (s != null && s.length > 0)
				map.set(name, s);
		} else
			for (i in 0...size) {
				final s = array.pop();
				if (s != null && s.length > 0)
					map.set(name + i, s);
			}
	}

	public static function start() {
		return new RegexLeaf(0, "^");
	}

	public static function end() {
		return new RegexLeaf(0, "$");
	}

	public static function spaceZeroOrMore() {
		return new RegexLeaf(0, "[%s]*");
	}

	public static function spaceOneOrMore() {
		return new RegexLeaf(0, "[%s]+");
	}
}
