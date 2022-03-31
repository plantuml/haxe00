package com.plantuml.utils;

class TreeSet<X> implements Set<X> {
	final tree = new BalancedTree<X, String>();
}
