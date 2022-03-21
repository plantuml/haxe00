package com.plantuml.utils;

import com.plantuml.core.DiagramType;
import com.plantuml.core.DiagramType.DiagramTypeUtils;

using hx.strings.Strings;

class StartUtils {
	static public function beforeStartUml(s:String):String {
		final x = s.indexOf("@start");
		if (x == -1)
			return null;
		return s.substr(0, x);
	}

	static public function removeHeader(s:String, header:String):String {
		if (header != null && s.startsWith(header))
			return s.substring(header.length);
		return s;
	}

	static public function isArobaseStartDiagram(s:String) {
		final s2 = s.trim();
		if (s2.startsWith("@") == false && s2.startsWith("\\") == false)
			return false;

		return DiagramTypeUtils.getTypeFromArobaseStart(s2) != DiagramType.UNKNOWN;
	}

	static public function startsWithSymbolAnd(tmp:String, value:String) {
		return tmp.startsWith("@" + value) || tmp.startsWith("\\" + value);
	}
}
