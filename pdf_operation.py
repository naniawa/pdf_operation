from tkinterdnd2 import *
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
from PyPDF2 import PdfFileReader
import os
"""
def add_listbox(event):
    if event.data.endswith(".pdf"):
        listbox.insert("end", event.data)
"""
def add_listbox(event):
    files = event.data.split()  # スペースで区切られたファイルパスを分割
    for file in files:
        if file.endswith(".pdf"):
            listbox.insert("end", file)
"""
def pdf_add():  # pdfファイルを結合
    # アウトプットPDFファイル名を指定するポップアップ表示
    filename = filedialog.asksaveasfilename(
        title = "結合するPDFファイル名を指定してください",
        filetypes = [("pdf", ".pdf") ], # ファイルフィルタ
        initialdir = "./", # 自分自身のディレクトリ
        defaultextension = "pdf")
    if filename == '':
        return
    merger = PyPDF2.PdfFileMerger(strict=False)
    for i in range(listbox.size()):
        merger.append(listbox.get(i))
    merger.write(filename)
    merger.close()
"""

def pdf_add():  # PDF ファイルを結合
    # アウトプット PDF ファイル名を指定するポップアップ表示
    filename = filedialog.asksaveasfilename(
        title="結合する PDF ファイル名を指定してください",
        filetypes=[("pdf", ".pdf")],  # ファイルフィルタ
        initialdir="./",  # 自分自身のディレクトリ
        defaultextension="pdf")
    if filename == '':
        return
    merger = PyPDF2.PdfFileMerger(strict=False)
    for i in range(listbox.size()):
        merger.append(listbox.get(i))
    merger.write(filename)
    merger.close()
    messagebox.showinfo("Success", "PDF pages split and saved successfully.")

def pdf_cut():  # pdfファイルを分割
    cut_dir = filedialog.askdirectory(title = "分割したファイルを保存するフォルダを選択してください",
        initialdir = './') 
    if cut_dir == '':
        return
    for i in range(listbox.size()):
        reader = PdfFileReader(listbox.get(i)) 
        for j in range(reader.getNumPages()):
            merger = PyPDF2.PdfFileMerger(strict=False)
            merger.append(listbox.get(i), pages=(j,j+1))
            cut_file = cut_dir + '/' + os.path.splitext(os.path.basename(listbox.get(i)))[0]
            merger.write(cut_file + '_' + str(j) + '.pdf')
            merger.close()
            messagebox.showinfo("Success", "PDF pages split and saved successfully.")

def del_listbox():  # 選択したファイルをLISTBOXからクリア
    indices = listbox.curselection()
    if len(indices) == 1:
        listbox.delete(indices)

def all_del_list(): # LISTBOXをクリア
    listbox.delete(0,listbox.size())

def up_list():  # 選択したLISTを1行アップ
    indices = listbox.curselection()
    if len(indices) == 1:   #選択した項目が１つか？
        if indices[0] > 0:
            listbox.insert(indices[0] - 1,listbox.get(indices))
            listbox.delete(indices[0] + 1)
            listbox.select_set(indices[0] - 1)

def down_list():    # 選択したLISTを1行ダウン
    indices = listbox.curselection()
    if len(indices) == 1:   #選択した項目が１つか？
        if indices[0] < listbox.size()-1:
            listbox.insert(indices[0] + 2,listbox.get(indices))
            listbox.delete(indices)
            listbox.select_set(indices[0] + 1)

# メインウィンドウの生成
root = TkinterDnD.Tk()
root.title('PDFファイルを結合＆分割')
root.geometry('400x400')
root.config(bg='#cccccc')

# Frameウィジェットの生成
frame = Frame(root)
# Listboxウィジェットの生成
listbox = Listbox(frame, width=50, height=15, selectmode=SINGLE)
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', add_listbox)

# スクロールバーの生成
scroll = Scrollbar(frame, orient=VERTICAL)
listbox.configure(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

# ウィジェットの配置
frame.place(x=20, y=20)
listbox.pack(fill=X, side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

# ボタンを定義
btn = tk.Button(root, text='結合', command=pdf_add)
btn2 = tk.Button(root, text='分割', command=pdf_cut)
btn3 = tk.Button(root, text='クリア', command=del_listbox)
btn4 = tk.Button(root, text='全てクリア', command=all_del_list)
btn_up = tk.Button(root, text='▲', command=up_list)
btn_down = tk.Button(root, text='▼', command=down_list)

# ボタンを配置
btn.place(x=40, y=300,width = 60)
btn2.place(x=120, y=300,width = 60)
btn3.place(x=200, y=300,width = 60)
btn4.place(x=280, y=300,width = 60)
btn_up.place(x=350, y=100,width = 40)
btn_down.place(x=350, y=150,width = 40)

root.mainloop()