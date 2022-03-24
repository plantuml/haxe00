package com.plantuml.ugraphic.color;

class HColorSet {
	public static function getColor(s):HColor {
		if (s == null) {
			trace('s=$s');
		}
		final theColor:Color = s;
		return new HColorSimple(theColor, false);
	}
}
