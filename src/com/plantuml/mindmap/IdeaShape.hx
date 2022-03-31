package com.plantuml.mindmap;

@:enum
abstract IdeaShape(String) {
	final BOX;
	final NONE;

	public static function fromDesc(s:String):IdeaShape {
		if ("_" == s)
			return NONE;

		return BOX;
	}
}
