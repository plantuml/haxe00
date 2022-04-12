package com.plantuml.real;

class RealDelta extends RealMoveable {
	private final delegated:Real;
	private final diff:Float;

	function new(delegated:Real, diff:Float) {
		final line = cast(delegated, AbstractReal).getLine();
		super(line, "[Delegated {" + delegated.getName() + "} d=" + diff + "]");
		this.delegated = delegated;
		this.diff = diff;
	}

	public function getCurrentValueInternal() {
		return delegated.getCurrentValue() + diff;
	}

	public function addAtLeast(delta:Float):Real {
		return new RealDelta(delegated.addAtLeast(delta), diff);
	}

	public function ensureBiggerThan(other:Real) {
		delegated.ensureBiggerThan(new RealDelta(other, -diff));
	}

	public function move(delta:Float) {
		cast(delegated, RealMoveable).move(delta);
	}
}
