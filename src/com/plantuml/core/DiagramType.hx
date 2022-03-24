package com.plantuml.core;

using com.plantuml.utils.StartUtils;

@:enum
abstract DiagramType(String) {
	final UNKNOWN;
	final MINDMAP;

	static public function getTypeFromArobaseStart(s:String):DiagramType {
		if (s.startsWithSymbolAnd("startmindmap"))
			return MINDMAP;
		return UNKNOWN;
	}
}
// class DiagramTypeUtils {
// 	static public function getTypeFromArobaseStart(s:String):DiagramType {
// 		if (s.startsWithSymbolAnd("startmindmap"))
// 			return MINDMAP;
// 		return UNKNOWN;
// 	}
// }
