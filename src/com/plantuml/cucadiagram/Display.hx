package com.plantuml.cucadiagram;

class Display {
	final displayData:Array<String>;

	private function new() {
		this.displayData = [];
	}

	public static function getWithNewlines(label:String) {
		final r = new Display();
		r.displayData.push(label);
		return r;
	}

	public static function create(lines:Array<String>):Display {
		final r = new Display();
		for (s in lines)
			r.displayData.push(s);
		return r;
	}

	public function getEndingStereotype():String {
		return null;
	}

	public function removeEndingStereotype():Display {
		return this;
	}

	public function get(i:Int):String {
		return displayData[i];
	}

	// public function toString():String {
	// 	return label;
	// }
}
