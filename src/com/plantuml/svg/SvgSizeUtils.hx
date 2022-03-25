package com.plantuml.svg;

using hx.strings.Strings;

class SvgSizeUtils {
	public static function singleSize(c:Int):Int {
		final v1 = SvgSizeAsciiUtils.asciiSize(c);
		if (v1!=0)
			return v1;
		// switch (c) {
		// 	case 0xA1:
		// 		return asciiSize("!".code);
		// 		case 0xA2:
		// 			return asciiSize("0".code);
		// 	}
			return 1500;


	}
}

