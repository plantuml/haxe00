package com.plantuml.real;

interface Real {
	// public void printCreationStackTrace();
	public function getName():String;
	public function getCurrentValue():Float;
	public function addFixed(delta:Float):Real;
	public function addAtLeast(delta:Float):Real;
	public function ensureBiggerThan(other:Real):Void;
}
