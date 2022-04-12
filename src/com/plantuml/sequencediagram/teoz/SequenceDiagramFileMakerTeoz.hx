package com.plantuml.sequencediagram.teoz;

import com.plantuml.sequencediagram.rose.Rose;

class SequenceDiagramFileMakerTeoz {
	//	private Dolls dolls;
	private final stringBounder:StringBounder;
	//
	//	private final TextBlock footer;
	//	private final TextBlock header;
	//
	//	private final PlayingSpaceWithParticipants body;
	//
	//	private final TextBlock title;
	//	private final TextBlock legend;
	//	private final TextBlock caption;
	//	private final Dimension2D dimTotal;
	//	private final Real min1;
	//
	//	private final LivingSpaces livingSpaces = new LivingSpaces();
	//	private final double heightEnglober1;
	//	private final double heightEnglober2;
	private final diagram:SequenceDiagram;
	private final fileFormatOption:FileFormatOption;
	private final skin:Rose;

	// private final AnnotatedWorker annotatedWorker;
	// private final int index;
	public function new(diagram:SequenceDiagram, skin:Rose, fileFormatOption:FileFormatOption, index:Int) {
		//		this.index = index;
		this.stringBounder = fileFormatOption.getDefaultStringBounder(diagram.getSkinParam());
		this.diagram = diagram;
		this.fileFormatOption = fileFormatOption;
		this.skin = skin;
		//		this.body = new PlayingSpaceWithParticipants(createMainTile());
		//		this.footer = getFooterOrHeader(FontParam.FOOTER);
		//		this.header = getFooterOrHeader(FontParam.HEADER);
		//		this.annotatedWorker = new AnnotatedWorker(diagram, diagram.getSkinParam(), stringBounder);
		//
		//		this.min1 = body.getMinX(stringBounder);
		//
		//		this.title = getTitle();
		//		this.legend = getLegend();
		//		this.caption = annotatedWorker.getCaption();
		//
		//		this.heightEnglober1 = dolls.getOffsetForEnglobers(stringBounder);
		//		this.heightEnglober2 = heightEnglober1 == 0 ? 0 : 10;
		//
		//		final double totalWidth = MathUtils.max(body.calculateDimension(stringBounder).getWidth(),
		//				title.calculateDimension(stringBounder).getWidth(), footer.calculateDimension(stringBounder).getWidth(),
		//				header.calculateDimension(stringBounder).getWidth(),
		//				legend.calculateDimension(stringBounder).getWidth());
		//		final double totalHeight = body.calculateDimension(stringBounder).getHeight() + heightEnglober1
		//				+ heightEnglober2 + title.calculateDimension(stringBounder).getHeight()
		//				+ header.calculateDimension(stringBounder).getHeight()
		//				+ legend.calculateDimension(stringBounder).getHeight()
		//				+ caption.calculateDimension(stringBounder).getHeight()
		//				+ footer.calculateDimension(stringBounder).getHeight() + (annotatedWorker.hasMainFrame() ? 10 : 0);
		//		this.dimTotal = new Dimension2DDouble(totalWidth, totalHeight);
	}

	public function drawInternal(ug:UGraphic, index:Int) {}
}
