package com.plantuml.ugraphic;

import com.plantuml.graphic.StringBounder;

interface UGraphic {
	public function getStringBounder():StringBounder;

	public function apply(change:UChange):UGraphic;

	public function draw(shape:UShape):Void;
}
