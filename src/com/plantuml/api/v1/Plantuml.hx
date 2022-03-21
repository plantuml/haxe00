package com.plantuml.api.v1;

using hx.strings.Strings;
using com.plantuml.utils.StartUtils;

import com.plantuml.ugraphic.UGraphicSvg;
import com.plantuml.command.BlocLines;
import com.plantuml.mindmap.MindMapDiagramFactory;

@:expose
class Plantuml {
	private var format:String = "svg";

	private var data:Array<String> = [];

	public function new() {}

	public function addLineSingle(line:String) {
		if (line != "")
			data[data.length] = line;
	}

	public function addLines(lines:String) {
		for (s in lines.split("\n"))
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
		var factory = new MindMapDiagramFactory();
		var lines = new BlocLines(data);

		var diagram = factory.createSystem(lines);
		var svg:UGraphicSvg = UGraphicSvg.create();
		diagram.exportDiagramNow(svg);
		var s = svg.getSvg();
		return s;
	}

	public function getInternalText() {
		var headerToRemove = null;
		var result = null;
		for (s in data) {
			final tmp = s.beforeStartUml();
			if (tmp != null)
				headerToRemove = tmp;
			s = s.removeHeader(headerToRemove);

			if (s.isArobaseStartDiagram())
				result = [];

			if (result != null)
				result.push(s);

			if (s.isArobaseEndDiagram())
				return result;
		}
		return null;
	}
}
