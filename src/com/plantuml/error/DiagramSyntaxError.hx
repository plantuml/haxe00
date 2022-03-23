package com.plantuml.error;

import com.plantuml.ugraphic.UText;
import com.plantuml.ugraphic.UGraphic;
import com.plantuml.core.Diagram;

class DiagramSyntaxError extends Diagram {
	final line:String;

	public function new(line:String) {
		this.line = line;
	}

	public function exportDiagramNow(ug:UGraphic) {
		ug.draw(new UText("DiagramSyntaxError at " + line));
	}
}
