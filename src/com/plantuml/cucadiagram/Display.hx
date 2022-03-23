package com.plantuml.cucadiagram;

import com.plantuml.ugraphic.UTranslate;
import com.plantuml.ugraphic.UText;
import com.plantuml.ugraphic.UFont;
import com.plantuml.ugraphic.UGraphic;
import com.plantuml.graphic.StringBounder;
import com.plantuml.awt.geom.Dimension2D;
import com.plantuml.graphic.TextBlock;

class Display {
	final displayData:Array<String>;

	private function new() {
		this.displayData = [];
	}

	public static function getWithNewlines(label:String) {
		final r = new Display();
		r.displayData.push(label);
		return r;
	}

	public static function create(lines:Array<String>):Display {
		final r = new Display();
		for (s in lines)
			r.displayData.push(s);
		return r;
	}

	public function getEndingStereotype():String {
		return null;
	}

	public function removeEndingStereotype():Display {
		return this;
	}

	public function get(i:Int):String {
		return displayData[i];
	}

	// public function toString():String {
	// 	return label;
	// }

	public function toTextBlock():TextBlock {
		return new Simple(displayData);
	}
}

class Simple implements TextBlock {
	final displayData:Array<String>;

	public function new(displayData:Array<String>) {
		this.displayData = displayData;
	}

	public function drawU(ug:UGraphic) {
		var y = 0.;
		final font = new UFont();
		for (s in displayData) {
			ug.apply(UTranslate.dy(y)).draw(new UText(s));
			final dim = ug.getStringBounder().calculateDimension(font, s);
			y += dim.getHeight();
		}
	}

	public function calculateDimension(stringBounder:StringBounder):Dimension2D {
		var width = 0.;
		var height = 0.;
		final font = new UFont();
		for (s in displayData) {
			final dim = stringBounder.calculateDimension(font, s);
			width = Math.max(width, dim.getWidth());
			height += dim.getHeight();
		}
		return new Dimension2D(width, height);
	}
}
