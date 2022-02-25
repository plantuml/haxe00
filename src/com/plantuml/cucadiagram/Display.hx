package com.plantuml.cucadiagram;

class Display {
	final label:String;

	private function new(label:String) {
		this.label = label;
	}

	public static function getWithNewlines(label:String) {
		return new Display(label);
	}

	public function getEndingStereotype():String {
		return null;
	}

	public function removeEndingStereotype():Display {
		return this;
	}

	public function get(i:Int):String {
		return label;
	}

	public function toString():String {
		return label;
	}
}
