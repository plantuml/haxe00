package com.plantuml.real;

abstract class RealMoveable extends AbstractReal implements Real {
	// public static final AtomicInteger CPT = new AtomicInteger();
	// private final int cpt = CPT.getAndIncrement();
	private final name:String;

	// private final Throwable creationPoint;

	public function new(line:RealLine, name) {
		super(line);
		this.name = name;
		// this.creationPoint = new Throwable();
		// this.creationPoint.fillInStackTrace();
	}

	abstract public function move(delta:Float):Void;

	// final public void printCreationStackTrace() {
	// 	creationPoint.printStackTrace();
	// }

	final public function addFixed(delta:Float):Real {
		return new RealDelta(this, delta);
	}

	// @Override
	// public final String toString() {
	// 	return "#" + cpt + "_" + name;
	// }

	final public function getName() {
		return name;
	}
}
