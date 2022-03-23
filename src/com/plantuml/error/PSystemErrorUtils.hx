package com.plantuml.error;

import com.plantuml.core.Diagram;

class PSystemErrorUtils {
	public static function syntaxErrorAt(s:String):Diagram {
		return new DiagramSyntaxError(s);
	}
}
