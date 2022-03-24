package com.plantuml.error;

import com.plantuml.command.BlocLines;
import com.plantuml.core.Diagram;
import com.plantuml.cucadiagram.Display;
import com.plantuml.graphic.FontConfiguration;
import com.plantuml.ugraphic.UGraphic;
import com.plantuml.ugraphic.UTranslate;
import com.plantuml.ugraphic.color.Color;
import com.plantuml.ugraphic.color.HColor;

class DiagramSyntaxError extends Diagram {
	final lines:BlocLines;

	public function new(lines:BlocLines) {
		this.lines = lines;
	}

	public function exportDiagramNow(ug:UGraphic) {
		final back:Color = "#000000";
		ug.applySetting(GeneralBackground(back));

		final display = lines.toDisplay();
		final textBlock = display.toTextBlock(FontConfiguration.create(HColor.plain("#00FF00")));
		textBlock.drawU(ug);
		final dim = textBlock.calculateDimension(ug.getStringBounder());

		ug = ug.apply(UTranslate.dy(dim.getHeight()));
		final err = Display.create(["^^^^^^^^^^^", "Syntax Error ?"]);
		err.toTextBlock(FontConfiguration.create(HColor.plain("#FF0000"))).drawU(ug);
	}
}
