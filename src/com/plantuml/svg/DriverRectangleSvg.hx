package com.plantuml.svg;

import com.plantuml.ugraphic.URectangle;
import com.plantuml.ugraphic.UText;
import com.plantuml.ugraphic.UShape;
import com.plantuml.ugraphic.color.ColorMapper;
import com.plantuml.ugraphic.UParam;
import com.plantuml.ugraphic.UDriver;

class DriverRectangleSvg implements UDriver {
	public function new() {}

	public function draw(shape:UShape, x:Float, y:Float, mapper:ColorMapper, param:UParam, object:SvgGraphics) {
		final rect = cast(shape, URectangle);

		final width = rect.getWidth();
		final height = rect.getHeight();

		final rx = 0;
		final ry = 0;

		object.svgRectangle(x, y, width, height, rx / 2, ry / 2, rect.getDeltaShadow(), rect.getComment(),
		rect.getCodeLine());


	}
}
