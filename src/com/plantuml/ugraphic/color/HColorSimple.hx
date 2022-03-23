package com.plantuml.ugraphic.color;

class HColorSimple implements HColor {
	final color:Color;
	final monochrome:Bool;

	public function new(color:Color, monochrome:Bool) {
		this.color = color;
		this.monochrome = monochrome;
	}
}
