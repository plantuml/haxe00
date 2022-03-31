package com.plantuml;

class ArrayExtensions {
	public static inline function last<T>(a:Array<T>):T {
		return a[a.length - 1];
	}

	public static inline function removeFirstAndLast<T>(a:Array<T>):Array<T> {
		return a.slice(1, a.length - 1);
	}

	public static function removeNullValue(m:Map<String, String>):String {
		final result = new BalancedTree<String, String>();
		for (key => value in m)
			if (value != null)
				result.set(key, value);
		return result.toString();
	}
}
