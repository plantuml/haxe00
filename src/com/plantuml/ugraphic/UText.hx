package com.plantuml.ugraphic;

class UText implements UShape {
	private final text:String;

	public function new(text:String) {
		this.text = text;
	}

	public function getText():String {
		return text;
	}
}
