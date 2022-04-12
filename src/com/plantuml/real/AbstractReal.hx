package com.plantuml.real;

abstract class AbstractReal implements Real {
	private final line:RealLine;

	function new(line) {
		this.line = line;
		this.line.register2(this);
	}

	final function getLine() {
		return line;
	}

	abstract function getCurrentValueInternal():Float;

	final public function getCurrentValue():Float {
		final result:Float = getCurrentValueInternal();
		return result;
	}

	public function getMaxAbsolute():Real {
		return line.asMaxAbsolute();
	}

	public function getMinAbsolute():Real {
		return line.asMinAbsolute();
	}
}
