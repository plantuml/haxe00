package com.plantuml;

class SkinParam implements ISkinParam {
	public function new() {}

	public function getCurrentStyleBuilder():StyleBuilder {
		return new StyleBuilder();
	}

	public function getThemeStyle():ThemeStyle {
		return ThemeStyle.LIGHT_REGULAR;
	}
}
