package com.plantuml.real;

class RealImpl extends RealMoveable implements RealOrigin {
	private var currentValue:Float;

	public function new(name:String, line:RealLine, currentValue:Float) {
		super(line, name);
		this.currentValue = currentValue;
	}

	function move(delta) {
		this.currentValue += delta;
	}

	function getCurrentValueInternal():Float {
		return currentValue;
	}

	public function addAtLeast(delta:Float):Real {
		final result = new RealImpl(getName() + ".addAtLeast" + delta, getLine(), this.currentValue + delta);
		getLine().addForce(new PositiveForce(this, result, delta));
		return result;
	}

	public function ensureBiggerThan(other:Real) {
		getLine().addForce(new PositiveForce(other, this, 0));
	}

	public function compileNow() {
		getLine().compile();
	}
}
