package com.plantuml.ugraphic;

class UTranslate implements UChange {
	private final dx:Float;
	private final dy:Float;

	public function new(dx:Float, dy:Float) {
		this.dx = dx;
		this.dy = dy;
	}

	public function getDx():Float {
		return dx;
	}

	public function getDy():Float {
		return dy;
	}

	public function copy():UTranslate {
		return new UTranslate(dx, dy);
	}

	public function compose(other:UTranslate):UTranslate {
		return new UTranslate(dx + other.dx, dy + other.dy);
	}
}
