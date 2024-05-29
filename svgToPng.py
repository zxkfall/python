import cairosvg

for size in [16, 32, 64, 128, 256, 512, 1024]:
    # 定义输入的SVG文件和输出的PNG文件
    svg_file = 'maple.svg'
    png_file = 'maple-' + str(size) + '.png'
    # 定义输出的PNG的宽度和高度（以像素为单位）
    width_px = size
    height_px = size

    # 使用cairosvg进行转换，并指定输出尺寸
    cairosvg.svg2png(url=svg_file, write_to=png_file, output_width=width_px, output_height=height_px)