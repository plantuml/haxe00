package com.plantuml.command;

class BlocLines {
	var lines:Array<String>;

	public function new(lines:Array<String>) {
		this.lines = lines.copy();
	}

	public function getLines() {
		return lines;
	}

	function toString():String {
		return lines.toString();
	}

	public function size() {
		return lines.length;
	}

	public static function single(s:String):BlocLines {
		return new BlocLines([s]);
	}
}
