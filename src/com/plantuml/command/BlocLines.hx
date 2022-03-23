package com.plantuml.command;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

class BlocLines {
	var lines:Array<String>;

	public function new(?lines:Array<String> = null) {
		if (lines == null)
			this.lines = [];
		else
			this.lines = lines.copy();
	}

	public function getLines() {
		return lines;
	}

	function toString():String {
		return lines.toString();
	}

	public function getFirst() {
		if (lines.length == 0)
			return null;
		return lines[0];
	}

	public function getLast() {
		return lines[lines.length - 1];
	}

	public function size() {
		return lines.length;
	}

	public static function single(s:String):BlocLines {
		return new BlocLines([s]);
	}

	public function addLineSingle(line:String) {
		lines[lines.length] = line;
	}

	public function addLines(lines:String) {
		for (s in lines.splitInLines())
			addLineSingle(s);
	}

	public function findStartSomething():BlocLines {
		var headerToRemove = null;
		var result = null;
		for (s in lines) {
			final tmp = s.beforeStartUml();
			if (tmp != null)
				headerToRemove = tmp;
			s = s.removeHeader(headerToRemove);

			if (s.isArobaseStartDiagram())
				result = [];

			if (result != null)
				result.push(s);

			if (s.isArobaseEndDiagram())
				return new BlocLines(result);
		}
		return null;
	}
}
