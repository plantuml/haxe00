package com.plantuml.error;

import com.plantuml.core.Diagram;
import com.plantuml.cucadiagram.Display;
import com.plantuml.graphic.FontConfiguration;
import com.plantuml.ugraphic.UGraphic;
import com.plantuml.ugraphic.color.Color;
import com.plantuml.ugraphic.color.HColor;
import haxe.CallStack;
import haxe.Exception;

class DiagramCrash extends Diagram {
	public function new(e:Exception) {
		trace(e.message);
		final st:CallStack = e.stack;
		for (item in st) {
			trace('item=$item');
		}
	}

	public function exportDiagramNow(ug:UGraphic) {
		final back:Color = "#000000";
		ug.applySetting(GeneralBackground(back));

		final err = Display.create(["DiagramCrash"]);
		err.toTextBlock(FontConfiguration.create(HColor.plain("#FF0000"))).drawU(ug);
	}
}
