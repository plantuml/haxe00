package com.plantuml.sequencediagram.teoz;

class TileArguments implements Bordered {
	private final stringBounder:StringBounder;
	private final origin:Real;
	private final livingSpaces:LivingSpaces;
	private final skin:Rose;
	private final skinParam:ISkinParam;
	private var bordered:Bordered;

	public function new(stringBounder:StringBounder, livingSpaces:LivingSpaces, skin:Rose, skinParam:ISkinParam, origin:Real) {
		this.stringBounder = stringBounder;
		this.origin = origin;
		this.livingSpaces = livingSpaces;
		this.skin = skin;
		this.skinParam = skinParam;
	}

	public function getBorder1():Float {
		return bordered.getBorder1();
	}

	public function getBorder2():Float {
		return bordered.getBorder2();
	}

	public function setBordered(bordered) {
		this.bordered = bordered;
	}
}
