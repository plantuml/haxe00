package com.plantuml.graphic;

import com.plantuml.ugraphic.color.HColor;

class FontConfiguration {
	final currentColor:HColor;

	private function new(currentColor:HColor) {
		this.currentColor = currentColor;
	}

	public static function create(currentColor:HColor) {
		return new FontConfiguration(currentColor);
	}

	public function getColor() {
		return currentColor;
	}
}
