package com.plantuml;

class SkinParam implements ISkinParam {
	public function new() {}

	public function getCurrentStyleBuilder():StyleBuilder {
		return new StyleBuilder();
	}
}
