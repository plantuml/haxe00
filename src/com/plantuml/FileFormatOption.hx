package com.plantuml;

import com.plantuml.ugraphic.UGraphicSvg.StringBounderSvg;

class FileFormatOption {
	public function new() {}

	public function getDefaultStringBounder(skinParam:SkinParam):StringBounder {
		return new StringBounderSvg();
	}
}
