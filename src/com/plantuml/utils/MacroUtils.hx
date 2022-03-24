package com.plantuml.utils;

class MacroUtils {
	public static macro function buildTime():haxe.macro.Expr.ExprOf<Int> {
		final buildTime = Math.floor(Date.now().getTime() / 1000);
		return macro $v{buildTime};
	}
}
