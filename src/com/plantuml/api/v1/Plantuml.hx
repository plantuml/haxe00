package com.plantuml.api.v1;

import com.plantuml.command.BlocLines;
import com.plantuml.mindmap.MindMapDiagramFactory;
import com.plantuml.ugraphic.UGraphicSvg;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;

@:expose
class Plantuml {
	private var format:String = "svg";

	private var data:Array<String> = [];

	public function new() {}

	public function addLineSingle(line:String) {
		data[data.length] = line;
	}

	public function addLines(lines:String) {
		for (s in lines.splitLines())
			addLineSingle(s);
	}

	public function addLinesArray(lines:Array<String>) {
		for (s in lines)
			addLineSingle(s);
	}

	public function toString() {
		return data.toString();
	}

	public function setFormat(arg0:String) {}

	public function setSvgLinkTarget(arg0:String) {}

	public function setWatermark(arg0:String) {}

	public function setScale(arg0:Float) {}

	public function setStyle(arg0:String) {}

	public function compile() {
		for (s in data) {
			trace(s);
		}
	}

	public function getSvg():String {
		final builder = new PSystemBuilder();
		final diagram = builder.createPSystem(data);
		var svg:UGraphicSvg = UGraphicSvg.create();
		diagram.exportDiagramNow(svg);
		var s = svg.getSvg();
		return s;
	}
}
