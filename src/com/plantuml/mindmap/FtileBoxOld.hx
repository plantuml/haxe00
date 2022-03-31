package com.plantuml.mindmap;

class FtileBoxOld implements TextBlock {
	final padding:ClockwiseTopRightBottomLeft;
	final label:Display;
	final textBlock:TextBlock;

	public function new(label:Display, fontConfiguration:FontConfiguration) {
		this.label = label;
		this.padding = ClockwiseTopRightBottomLeft.same(10);
		this.textBlock = label.toTextBlock(fontConfiguration);
	}

	public static function createMindMap(style:Style, label:Display):TextBlock {
		return new FtileBoxOld(label, style.getFontConfiguration());
	}

	public function drawU(ug:UGraphic) {
		final dim2 = calculateDimension(ug.getStringBounder());

		ug = ug.apply(HColor.plain("#000000"));
		ug = ug.apply(HColor.plain("#CCCCCC").fill());
		ug.draw(new URectangle(dim2.getWidth(), dim2.getHeight()));

		ug = ug.apply(new UTranslate(padding.getLeft(), padding.getTop()));
		final dim = getDimRaw(ug.getStringBounder());
		// ug.draw(new URectangle(dim.getWidth(), dim.getHeight()));

		// ug.draw(new UText(label.get(0)));
		textBlock.drawU(ug);
	}

	function getDimRaw(stringBounder:StringBounder) {
		// return stringBounder.calculateDimension(new UFont(), label.get(0));
		return textBlock.calculateDimension(stringBounder);
	}

	public function calculateDimension(stringBounder:StringBounder):Dimension2D {
		var dimRaw = getDimRaw(stringBounder);
		dimRaw = dimRaw.delta(padding.getLeft() + padding.getRight(), padding.getBottom() + padding.getTop());
		return dimRaw;
	}
}
