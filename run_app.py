import csv
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
sys.path.insert(0,str(Path(__file__).resolve().parent/'src'))
from preference_core import preference_distance

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Preference Distance — Research Preview v0.2')
        self.geometry('850x550')
        self.columnconfigure(0,weight=1)
        ttk.Label(self,text='Preference Distance (VBA-compatible pairwise ordering)',font=('Segoe UI',13,'bold')).grid(row=0,column=0,pady=12)
        ttk.Label(self,text='One ranking per line, or comma/space separated. Ties are supported.').grid(row=1,column=0)
        panel=ttk.Frame(self);panel.grid(row=2,column=0,sticky='nsew',padx=16,pady=8)
        panel.columnconfigure(0,weight=1);panel.columnconfigure(1,weight=1)
        self.inputs=[]
        for j,title in enumerate(('Preference 1','Preference 2')):
            side=ttk.Frame(panel);side.grid(row=0,column=j,sticky='nsew',padx=7)
            ttk.Label(side,text=title).pack(anchor='w')
            t=tk.Text(side,height=17,width=32);t.pack(fill='both',expand=True)
            self.inputs.append(t)
            ttk.Button(side,text='Load TXT/CSV...',command=lambda k=j:self.load(k)).pack(pady=5)
        self.inputs[0].insert('1.0','1\n1\n5\n1\n2\n3\n4')
        self.inputs[1].insert('1.0','1\n2\n2\n2\n3\n4\n5')
        buttons=ttk.Frame(self);buttons.grid(row=3,column=0,pady=4)
        ttk.Button(buttons,text='Calculate',command=self.calc).pack(side='left',padx=8)
        ttk.Button(buttons,text='Save result (CSV)',command=self.save).pack(side='left',padx=8)
        self.output=tk.StringVar(value='Click Calculate to compare the two rankings.')
        ttk.Label(self,textvariable=self.output,font=('Consolas',11)).grid(row=4,column=0,pady=10)
        ttk.Label(self,text='Research Preview: validates the VBA distance calculation, not an inferential statistical test.',foreground='gray').grid(row=5,column=0,pady=4)
        self.result=None
    def load(self,k):
        path=filedialog.askopenfilename(filetypes=[('Text/CSV','*.txt *.csv'),('All files','*.*')])
        if path:
            try:
                contents=Path(path).read_text(encoding='utf-8-sig')
            except UnicodeDecodeError:
                contents=Path(path).read_text(encoding='cp1252')
            self.inputs[k].delete('1.0','end');self.inputs[k].insert('1.0',contents)
    def parse(self,k):
        import re
        content=self.inputs[k].get('1.0','end').strip()
        values=[float(z) for z in re.split(r'[,;\s]+',content) if z]
        return values
    def calc(self):
        try:
            self.result=preference_distance(self.parse(0),self.parse(1))
            self.output.set(f"Cosine = {self.result['cosine']:.9f}     Angular distance = {self.result['distance']:.9f}")
        except Exception as exc:
            self.result=None;messagebox.showerror('Invalid data',str(exc))
    def save(self):
        if self.result is None:
            messagebox.showinfo('No result','Calculate first.');return
        p=filedialog.asksaveasfilename(defaultextension='.csv',filetypes=[('CSV','*.csv')])
        if p:
            with open(p,'w',newline='',encoding='utf-8-sig') as f:
                w=csv.writer(f);w.writerow(['metric','value']);w.writerows(self.result.items())
if __name__=='__main__': App().mainloop()
