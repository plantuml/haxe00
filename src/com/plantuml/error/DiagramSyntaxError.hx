package com.plantuml.error;

import com.plantuml.ugraphic.color.Color;
import com.plantuml.ugraphic.UGeneralBackground;
import com.plantuml.ugraphic.UTranslate;
import com.plantuml.cucadiagram.Display;
import haxe.display.FsPath;
import com.plantuml.command.BlocLines;
import com.plantuml.ugraphic.UText;
import com.plantuml.ugraphic.UGraphic;
import com.plantuml.core.Diagram;

class DiagramSyntaxError extends Diagram {
	final lines:BlocLines;

	public function new(lines:BlocLines) {
		this.lines = lines;
	}

	public function exportDiagramNow(ug:UGraphic) {
		final back:Color = "#EE0000";
		ug.apply(new UGeneralBackground(back));

		final display = lines.toDisplay();
		final textBlock = display.toTextBlock();
		textBlock.drawU(ug);
		final dim = textBlock.calculateDimension(ug.getStringBounder());

		ug = ug.apply(UTranslate.dy(dim.getHeight()));
		final err = Display.create(["^^^^^^^^^^^", "Syntax Error ?"]);
		err.toTextBlock().drawU(ug);
	}
}
