package com.plantuml.core;

import com.plantuml.utils.AbstractEnumTools;

using com.plantuml.utils.StartUtils;

@:enum
abstract DiagramType(String) {
	final UNKNOWN;
	final MINDMAP;

	static public function getTypeFromArobaseStart(s:String):DiagramType {
		final all:Array<DiagramType> = AbstractEnumTools.getValues(DiagramType);

		for (t in all) {
			final lower:String = "start" + ("" + t).toLowerCase();
			if (s.startsWithSymbolAnd(lower))
				return t;
		}

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
