package com.plantuml.style;

import com.plantuml.ugraphic.color.HColorSet;
import com.plantuml.ugraphic.color.HColor;
import com.plantuml.graphic.FontConfiguration;

class Style {
	public function new() {}

	public function getFontConfiguration():FontConfiguration {
		return FontConfiguration.create(HColorSet.getColor("#0000FF"));
	}
}
