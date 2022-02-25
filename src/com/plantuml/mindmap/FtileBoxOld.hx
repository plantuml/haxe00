package com.plantuml.mindmap;

import com.plantuml.ugraphic.UTranslate;
import com.plantuml.style.ClockwiseTopRightBottomLeft;
import com.plantuml.ugraphic.URectangle;
import com.plantuml.ugraphic.UText;
import com.plantuml.ugraphic.UFont;
import com.plantuml.ugraphic.UGraphic;
import com.plantuml.graphic.StringBounder;
import com.plantuml.awt.geom.Dimension2D;
import com.plantuml.graphic.TextBlock;
import com.plantuml.cucadiagram.Display;
import com.plantuml.style.StyleBuilder;

class FtileBoxOld implements TextBlock {
	final padding:ClockwiseTopRightBottomLeft;
	final label:Display;

	public function new(label:Display) {
		this.label = label;
		this.padding = ClockwiseTopRightBottomLeft.same(10);
	}

	public static function createMindMap(styleBuilder:StyleBuilder, label:Display):TextBlock {
		return new FtileBoxOld(label);
	}

	public function drawU(ug:UGraphic) {
		final dim2 = calculateDimension(ug.getStringBounder());
		ug.draw(new URectangle(dim2.getWidth(), dim2.getHeight()));

		ug = ug.apply(new UTranslate(padding.getLeft(), padding.getTop()));
		final dim = getDimRaw(ug.getStringBounder());
		// ug.draw(new URectangle(dim.getWidth(), dim.getHeight()));

		ug.draw(new UText(label.get(0)));
	}

	function getDimRaw(stringBounder:StringBounder) {
		return stringBounder.calculateDimension(new UFont(), label.get(0));
	}

	public function calculateDimension(stringBounder:StringBounder):Dimension2D {
		var dimRaw = getDimRaw(stringBounder);
		dimRaw = dimRaw.delta(padding.getLeft() + padding.getRight(), padding.getBottom() + padding.getTop());
		return dimRaw;
	}
}
