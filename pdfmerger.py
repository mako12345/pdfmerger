import PyPDF2
import sys

# テキストファイルからファイルリストを取得する
file_list = open("./file_list.txt", "r", encoding="utf-8")

# 引数を入力している場合は処理を実施する
if len(sys.argv) == 3:

    merger = PyPDF2.PdfFileMerger()

    # テキストファイルのファイルリストにしたがってマージする
    for file in file_list:
        file = file.replace("\n","")
        merger.append('./data/' + file)

    # pdfファイルを出力する
    merger.write('./data/' + sys.argv[2])
    merger.close()
else:
    print("Please Input Argument..")

# ファイルを閉じる
file_list.close()