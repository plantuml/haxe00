package com.plantuml.core;

using com.plantuml.utils.StartUtils;

enum DiagramType {
	UNKNOWN;
	MINDMAP;
}

class DiagramTypeUtils {
	static public function getTypeFromArobaseStart(s:String):DiagramType {
		if (s.startsWithSymbolAnd("startmindmap"))
			return MINDMAP;
		return UNKNOWN;
	}
}
