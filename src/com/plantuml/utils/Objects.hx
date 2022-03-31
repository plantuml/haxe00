package com.plantuml.utils;

class Objects {
	public static inline function requireNonNull(x:Dynamic):Void {
		if (x == null)
			throw new NotImplementedException();
	}
}
