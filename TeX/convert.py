def convert_tex_file(input_file, output_file):
    with open(input_file, encoding="utf-8") as f:
        tex_content = f.read()

    converted_content = tex_content.replace("、", ",").replace("。", ".")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(converted_content)


# 使い方の例
input_tex_file = "3.tex"
output_tex_file = "output.tex"
convert_tex_file(input_tex_file, output_tex_file)
