package com.plantuml.real;

class RealLine {
	public function new() {}

	private final forces:Array<PositiveForce> = [];

	private var min:Float;
	private var max:Float;
	private final all:Set<AbstractReal> = new Set();

	public function register2(abstractReal:AbstractReal) {
		all.add(abstractReal);
	}

	public function getAbsoluteMin() {
		return min;
	}

	public function getAbsoluteMax() {
		return max;
	}

	public function addForce(force:PositiveForce) {
		this.forces.push(force);
	}

	//	static private int CPT;
	//
	public function compile() {
		throw new NotImplementedException();
	}

	//	public void compile() {
	//		int cpt = 0;
	//		final Map<PositiveForce, Integer> counter = new HashMap<PositiveForce, Integer>();
	//		do {
	//			boolean done = true;
	//			for (PositiveForce f : forces) {
	//				// System.err.println("force=" + f);
	//				final boolean change = f.apply();
	//				if (change) {
	//					incCounter(counter, f);
	//					// System.err.println("changed! " + f);
	//					done = false;
	//				}
	//			}
	//			if (done) {
	//				// System.err.println("cpt=" + cpt + " size=" + forces.size());
	//				CPT += cpt;
	//				// System.err.println("CPT=" + CPT);
	//				min = 0;
	//				max = 0;
	//				for (AbstractReal real : all) {
	//					final double v = real.getCurrentValue();
	//					// System.err.println("RealLine::compile v=" + v);
	//					if (v > max) {
	//						max = v;
	//					}
	//					if (v < min) {
	//						min = v;
	//					}
	//				}
	//				// System.err.println("RealLine::compile min=" + min + " max=" + max);
	//				return;
	//			}
	//			cpt++;
	//			if (cpt > 99999) {
	//				printCounter(counter);
	//				throw new IllegalStateException("Inifinite Loop?");
	//			}
	//		} while (true);
	//
	//	}
	//
	//	private void printCounter(Map<PositiveForce, Integer> counter) {
	//		for (PositiveForce f : forces) {
	//			System.err.println("force=" + f);
	//		}
	//		for (Map.Entry<PositiveForce, Integer> ent : counter.entrySet()) {
	//			System.err.println("count=" + ent.getValue() + " for " + ent.getKey());
	//		}
	//	}
	//
	//	private static void incCounter(Map<PositiveForce, Integer> counter, PositiveForce f) {
	//		final Integer v = counter.get(f);
	//		counter.put(f, v == null ? 1 : v + 1);
	//	}
	//
	public function asMaxAbsolute():Real {
		throw new haxe.exceptions.NotImplementedException();
	}

	public function asMinAbsolute():Real {
		throw new haxe.exceptions.NotImplementedException();
	}

	//	Real asMaxAbsolute() {
	//		return new MaxAbsolute();
	//	}
	//
	//	Real asMinAbsolute() {
	//		return new MinAbsolute();
	//	}
	//
	//	class MaxAbsolute extends AbstractAbsolute {
	//		public double getCurrentValue() {
	//			return max;
	//		}
	//	}
	//
	//	class MinAbsolute extends AbstractAbsolute {
	//		public double getCurrentValue() {
	//			return min;
	//		}
	//	}
	//
	//	abstract class AbstractAbsolute implements Real {
	//
	//		public void printCreationStackTrace() {
	//		}
	//
	//		public String getName() {
	//			return getClass().getName();
	//		}
	//
	//		public Real addFixed(double delta) {
	//			throw new UnsupportedOperationException();
	//		}
	//
	//		public Real addAtLeast(double delta) {
	//			throw new UnsupportedOperationException();
	//		}
	//
	//		public void ensureBiggerThan(Real other) {
	//			throw new UnsupportedOperationException();
	//		}
	//
	//		public Real getMaxAbsolute() {
	//			return asMaxAbsolute();
	//		}
	//
	//		public Real getMinAbsolute() {
	//			return asMinAbsolute();
	//		}
	//
	//	}
}
