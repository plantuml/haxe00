package com.plantuml.command.regex;

class RegexOr extends AbstractRegex implements IRegex {
	private final all:Array<IRegex>;
	private final name:String;

	public function getSize():Int {
		var size = 0;
		for (r in all)
			size += r.getSize();
		return size;
	}

	public function new(?name:String, all:Array<IRegex>) {
		this.name = name;
		this.all = all;
		var tmp:String = "";
		for (r in all) {
			if (tmp.length == 0)
				tmp += name == null ? "(?:" : "(";
			else
				tmp += "|";
			tmp += r.getPatternString();
		}
		tmp += ")";
		super(tmp);
	}

	public function eat(array:Array<String>, map:Map<String, String>):Void {
		if (name != null) {
			final s = array.pop();
			map.set(name, s);
		}
		for (r in all)
			r.eat(array, map);
	}
}
