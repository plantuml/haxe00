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
		final height = 16.0;
		var width = 0.0;
		for (c in new haxe.iterators.StringIteratorUnicode(text)) {
			// trace("" + c.toChar());
			width += singleSize(c) / 100.0;
		}
		return new Dimension2D(width, height);
	}

	private function singleSize(c) {
		switch (c) {
			case " ".code:
				return 500;
			case "!".code:
				return 650;
			case "\"".code:
				return 740;
			case "#".code:
				return 1340;
			case "$".code:
				return 1020;
			case "%".code:
				return 1520;
			case "&".code:
				return 1430;
			case "'".code:
				return 440;
			case "(".code | ")".code:
				return 630;
			case "*".code:
				return 800;
			case "+".code:
				return 1340;
			case ",".code:
				return 510;
			case "-".code:
				return 550;
			case ".".code:
				return 510;
			case "/".code:
				return 540;
			case "0".code | "1".code | "2".code | "3".code | "4".code | "5".code | "6".code | "7".code | "8".code | "9".code:
				return 1020;
			case ":".code:
				return 540;
			case ";".code:
				return 540;
			case "<".code | "=".code | ">".code:
				return 1340;
			case "?".code:
				return 860;
			case "@".code:
				return 1600;
			case "A".code:
				return 1160;
			case "B".code:
				return 1180;
			case "C".code:
				return 1230;
			case "D".code:
				return 1290;
			case "E".code:
				return 1170;
			case "F".code:
				return 1110;
			case "G".code:
				return 1280;
			case "H".code:
				return 1400;
			case "I".code:
				return 640;
			case "J".code:
				return 650;
			case "K".code:
				return 1200;
			case "L".code:
				return 1070;
			case "M".code:
				return 1640;
			case "N".code:
				return 1400;
			case "O".code:
				return 1320;
			case "P".code:
				return 1080;
			case "Q".code:
				return 1320;
			case "R".code:
				return 1210;
			case "S".code:
				return 1070;
			case "T".code:
				return 1100;
			case "U".code:
				return 1350;
			case "V".code:
				return 1160;
			case "W".code:
				return 1650;
			case "X".code:
				return 1140;
			case "Y".code:
				return 1060;
			case "Z".code:
				return 1120;
			case "[".code | "]".code:
				return 630;
			case "\\".code:
				return 540;
			case "^".code:
				return 1340;
			case "_".code:
				return 800;
			case "`".code:
				return 800;
			case "a".code:
				return 960;
			case "b".code:
				return 1030;
			case "c".code:
				return 900;
			case "d".code:
				return 1030;
			case "e".code:
				return 950;
			case "f".code:
				return 570;
			case "g".code:
				return 1030;
			case "h".code:
				return 1030;
			case "i".code:
				return 510;
			case "j".code:
				return 500;
			case "k".code:
				return 970;
			case "l".code:
				return 510;
			case "m".code:
				return 1520;
			case "n".code:
				return 1030;
			case "o".code:
				return 970;
			case "p".code:
				return 1030;
			case "q".code:
				return 1030;
			case "r".code:
				return 770;
			case "s".code:
				return 830;
			case "t".code:
				return 650;
			case "u".code:
				return 1030;
			case "v".code:
				return 910;
			case "w".code:
				return 1370;
			case "x".code:
				return 910;
			case "y".code:
				return 910;
			case "z".code:
				return 850;
			case "{".code | "}".code:
				return 1020;
			case "|".code:
				return 540;
			case "~".code:
				return 1340;
		}
		return 1500;
	}
}

class UGraphicSvg extends AbstractCommonUGraphic<SvgGraphics> implements UGraphic {
	private final core:SvgGraphics;

	private function new(core:SvgGraphics) {
		this.core = core;
		this.drivers.set(Type.getClassName(UText), new DriverTextSvg(new StringBounderSvg()));
		this.drivers.set(Type.getClassName(URectangle), new DriverRectangleSvg());
		this.drivers.set(Type.getClassName(UPath), new DriverPathSvg());
	}

	public override function apply(change:UChange):UGraphicSvg {
		var tmp1 = super.apply(change);
		return cast(tmp1, UGraphicSvg);
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
			driver.draw(shape, getTranslateX(), getTranslateY(), getColorMapper(), getParam(), core);
		}
	}

	public function getSvg():String {
		return core.toSvg();
	}

	function copyUGraphic():UGraphicSvg {
		var result = new UGraphicSvg(core);
		result.translate = this.translate.copy();
		result.color = this.color;
		result.backColor = this.backColor;
		return result;
	}
}
