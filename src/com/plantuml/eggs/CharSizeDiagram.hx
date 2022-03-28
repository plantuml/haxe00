package com.plantuml.eggs;

using com.plantuml.utils.StartUtils;
using hx.strings.Strings;
using com.plantuml.ArrayExtensions;

import com.plantuml.ugraphic.UTranslate;
import com.plantuml.ugraphic.URectangle;
import com.plantuml.ugraphic.UText;
import com.plantuml.ugraphic.color.HColor;
import com.plantuml.graphic.FontConfiguration;
import hx.strings.StringBuilder;
import com.plantuml.ugraphic.UGraphic;
import com.plantuml.core.Diagram;

class CharSizeDiagram extends Diagram {
	final single:String;
	final size:Int;

	public function new(single:String, size:Int) {
		this.single = single;
		this.size = size;
	}

	function getLongString(nb:Int) {
		final sb = new StringBuilder();
		for (i in 0...nb)
			sb.add(single);
		return sb.toString();
	}

	public function exportDiagramNow(ug:UGraphic) {
		final fc = FontConfiguration.create(HColor.plain("#000000"));

		final text = getLongString(64);
		final utext = new UText(text, fc);
		final sb = ug.getStringBounder();

		final dim = sb.calculateDimension(fc.getFont(), text);
		final width:Float = size / 100.0 * 64;
		final rect = new URectangle(width, dim.getHeight());
		final rectLong = new URectangle(width + 30, dim.getHeight());

		final num = StringTools.hex(single.charCodeAt(0));
		ug.draw(new UText(num, fc));

		final ug2 = ug.apply(UTranslate.dx(40));

		ug2.apply(HColor.plain("#FFFFFF")).draw(rectLong);
		ug2.apply(HColor.plain("#FF0000")).draw(rect);
		ug2.draw(utext);
	}
}
