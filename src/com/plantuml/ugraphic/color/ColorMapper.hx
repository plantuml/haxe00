package com.plantuml.ugraphic.color;

class ColorMapper {
	public function new() {}

	public function toColor(color:HColor):Color {
		return cast(color, HColorSimple).getColor();
	}

	public function toSvg(color:HColor):String {
		if (color == null)
			return "none";

		return "" + cast(color, HColorSimple).getColor();
	}
}
