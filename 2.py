import fitz  # PyMuPDF


def convert_pdf_to_images(pdf_file, image_prefix, dpi=300):
    # 打开PDF文件
    pdf_document = fitz.open(pdf_file)

    # 逐页将PDF转换为图像
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)

        # 设置图像的 DPI（每英寸点数）
        image = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))

        # 生成图像文件的名称，使用给定的前缀和页码
        image_filename = f"{image_prefix}_{page_number + 1}.png"

        # 保存图像为PNG文件
        image.save(image_filename, "png")

    # 关闭PDF文件
    pdf_document.close()


if __name__ == "__main__":
    # 指定输入的PDF文件、输出图像的前缀以及 DPI
    pdf_file = "2.pdf"
    image_prefix = "xixixi"
    dpi = 300  # 调整 DPI 以提高图像质量

    # 调用函数进行转换
    convert_pdf_to_images(pdf_file, image_prefix, dpi)
