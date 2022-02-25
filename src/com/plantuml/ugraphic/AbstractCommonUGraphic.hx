package com.plantuml.ugraphic;

abstract class AbstractCommonUGraphic implements UGraphic {
	var translate:UTranslate = new UTranslate(0, 0);
	final drivers:Map<String, UDriver> = [];

	function getTranslateX():Float {
		return translate.getDx();
	}

	function getTranslateY():Float {
		return translate.getDy();
	}

	public function apply(change:UChange):UGraphic {
		var result = copyUGraphic();
		if (change is UTranslate) {
			final translate = cast(change, UTranslate);
			result.translate = result.translate.compose(translate);
			return result;
		}

		throw new haxe.exceptions.NotImplementedException();
	}

	abstract function copyUGraphic():AbstractCommonUGraphic;
}
