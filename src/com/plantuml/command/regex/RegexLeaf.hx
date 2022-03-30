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
		if (size == 1)
			map.set(name, popFromArray(array));
		else
			for (i in 0...size)
				map.set(name + i, popFromArray(array));
	}

	private function popFromArray(array:Array<String>) {
		final s = array.pop();
		if (s != null && s.length == 0)
			return null;
		return s;
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
