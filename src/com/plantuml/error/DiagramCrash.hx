package com.plantuml.error;

import haxe.Exception;
import com.plantuml.command.BlocLines;
import com.plantuml.core.Diagram;
import com.plantuml.cucadiagram.Display;
import com.plantuml.graphic.FontConfiguration;
import com.plantuml.ugraphic.UGraphic;
import com.plantuml.ugraphic.UTranslate;
import com.plantuml.ugraphic.color.Color;
import com.plantuml.ugraphic.color.HColor;

class DiagramCrash extends Diagram {
	public function new(e:Exception) {}

	public function exportDiagramNow(ug:UGraphic) {
		final back:Color = "#000000";
		ug.applySetting(GeneralBackground(back));

		final err = Display.create(["DiagramCrash"]);
		err.toTextBlock(FontConfiguration.create(HColor.plain("#FF0000"))).drawU(ug);
	}
}
