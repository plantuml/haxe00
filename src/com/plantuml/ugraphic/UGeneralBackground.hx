package com.plantuml.ugraphic;

import com.plantuml.ugraphic.color.Color;

class UGeneralBackground implements UShape {
	final color:Color;

	public function new(color:Color) {
		this.color = color;
	}
}
