package com.plantuml.ugraphic.color;

import haxe.exceptions.NotImplementedException;

class HColorSimple implements HColor {
	final color:Color;
	final monochrome:Bool;

	public function new(color:Color, monochrome:Bool) {
		if (color == null)
			throw new NotImplementedException();

		this.color = color;
		this.monochrome = monochrome;
	}

	public function getColor() {
		return color;
	}
}
