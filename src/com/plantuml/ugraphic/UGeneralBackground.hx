package com.plantuml.ugraphic;

import com.plantuml.ugraphic.color.Color;

class UGeneralBackground implements UChange {
	final color:Color;

	public function new(color:Color) {
		this.color = color;
	}
}
