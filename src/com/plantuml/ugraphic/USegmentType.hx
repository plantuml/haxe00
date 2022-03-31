package com.plantuml.ugraphic;

@:enum
abstract USegmentType(String) {
	final SEG_MOVETO;
	final SEG_LINETO;
	final SEG_QUADTO;
	final SEG_CUBICTO;
	final SEG_CLOSE;
	final SEG_ARCTO;

	public static function getNbPoints(me:USegmentType):Int {
		switch (me) {
			case SEG_MOVETO:
				return 1;
			case SEG_LINETO:
				return 1;
			case SEG_CUBICTO:
				return 3;
			case SEG_CLOSE:
				return 0;
			default:
				throw new haxe.exceptions.NotImplementedException();
		}
		throw new haxe.exceptions.NotImplementedException();
	}
}
