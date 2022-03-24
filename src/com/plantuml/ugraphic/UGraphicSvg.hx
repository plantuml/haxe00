package com.plantuml.ugraphic;

import com.plantuml.ugraphic.color.Color;
import com.plantuml.svg.DriverPathSvg;
import com.plantuml.svg.DriverRectangleSvg;
import com.plantuml.svg.DriverTextSvg;
import com.plantuml.svg.SvgGraphics;

using hx.strings.Strings;

import com.plantuml.awt.geom.Dimension2D;
import com.plantuml.graphic.StringBounder;

class StringBounderSvg implements StringBounder {
	public function new() {}

	public function calculateDimension(font:UFont, text:String):Dimension2D {
		final width = text.length;
		final height = 16;
		return new Dimension2D(width * 12, height);
	}
}

class UGraphicSvg extends AbstractCommonUGraphic<SvgGraphics> implements UGraphic {
	private final core:SvgGraphics;

	public function new(core:SvgGraphics) {
		this.core = core;
		this.drivers.set(Type.getClassName(UText), new DriverTextSvg());
		this.drivers.set(Type.getClassName(URectangle), new DriverRectangleSvg());
		this.drivers.set(Type.getClassName(UPath), new DriverPathSvg());
	}

	public function applySetting(setting:USetting):Void {
		switch (setting) {
			case GeneralBackground(color):
				core.setGeneralBackground(color);
		}
	}

	public static function create():UGraphicSvg {
		return new UGraphicSvg(new SvgGraphics());
	}

	public function getStringBounder():StringBounder {
		return new StringBounderSvg();
	}

	public function draw(shape:UShape) {
		var cl = Type.getClass(shape);
		var driver = drivers.get(Type.getClassName(cl));
		if (driver == null) {
			trace(shape);
			throw new haxe.exceptions.NotImplementedException();
		} else {
			driver.draw(shape, getTranslateX(), getTranslateY(), null, null, core);
		}
	}

	public function getSvg():String {
		return core.toSvg();
	}

	function copyUGraphic():UGraphicSvg {
		var result = new UGraphicSvg(core);
		result.translate = this.translate.copy();
		return result;
	}
}
