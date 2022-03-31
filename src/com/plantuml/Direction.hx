package com.plantuml;

@:enum
abstract Direction(String) {
	final RIGHT;
	final LEFT;
	final DOWN;
	final UP;

	public static function valueOf(s:String):Direction {
		if (s == "RIGHT")
			return RIGHT;
		if (s == "LEFT")
			return LEFT;
		if (s == "DOWN")
			return DOWN;
		if (s == "UP")
			return UP;

		throw new NotImplementedException();
	}
}
