package com.plantuml.ugraphic.color;

class HColorSet {
	public static function getColor(s):HColor {
		final theColor:Color = s;
		return new HColorSimple(theColor, false);
	}
}
