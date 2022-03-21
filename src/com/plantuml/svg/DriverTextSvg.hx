package com.plantuml.svg;

import com.plantuml.ugraphic.UText;
import com.plantuml.ugraphic.UShape;
import com.plantuml.ugraphic.color.ColorMapper;
import com.plantuml.ugraphic.UParam;
import com.plantuml.ugraphic.UDriver;

class DriverTextSvg implements UDriver<SvgGraphics> {
	public function new() {}

	public function draw(shape:UShape, x:Float, y:Float, mapper:ColorMapper, param:UParam, object:SvgGraphics) {
		final text = cast(shape, UText);
		object.text(text.getText(), x, y + 12, "", 16, "", "plain", "", 100, [], "");
	}
}
