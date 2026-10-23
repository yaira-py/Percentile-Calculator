import customtkinter as ctk
import numpy as np

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

class PercentileApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Rank Based Percentile Calculator')
        self.geometry('600x550')
        self.configure(fg_color="#f0f0f0")

        hearder=ctk.CTkFrame(self,fg_color="#D8DDE6",corner_radius=8)
        hearder.pack(fill='x',padx=10,pady=10)

        ctk.CTkLabel(hearder,text='Rank Based Percentile Calculator',font=('Arial',20,'bold'),text_color='black').pack(anchor='w',
                                    padx=15,pady=(10,0))
        ctk.CTkLabel(hearder,text='Calculate your percentile rank based on total students and your rank',
                     font=('Arial',13),text_color='#333333').pack(anchor='w',padx=15,pady=(0,10))


        row1=ctk.CTkFrame(self,fg_color='#f0f0f0')
        row1.pack(fill='x',padx=20,pady=15)
        ctk.CTkLabel(row1,text='Total Students:',font=('Arial',16,'bold'),width=150).pack(side='left')
        self.total_entry=ctk.CTkEntry(row1,width=400,height=40,font=('Arial',16))
        self.total_entry.insert(0,'5000')
        self.total_entry.pack(side='left',padx=10)

        row2=ctk.CTkFrame(self,fg_color='#f0f0f0')
        row2.pack(fill='x',padx=20,pady=5)
        ctk.CTkLabel(row2,text='Your Rank:',font=('Arial',16,'bold'),width=150).pack(side='left')
        self.rank_entry=ctk.CTkEntry(row2,height=40,width=400,font=('Arial',16),text_color='#0A3D8F')
        self.rank_entry.insert(0,'385')
        self.rank_entry.pack(side='left',padx=10)

        self.btn=ctk.CTkButton(self,text='📟 Calculate',font=('Arial',16,'bold'),fg_color='#0B6ED7',height=45,width=180,command=self.calculate)
        self.btn.pack(pady=20)

        self.result_frame=ctk.CTkFrame(self,fg_color='#D8DDE6',corner_radius=10,border_width=1,border_color='#A9BEE0')
        self.result_frame.pack(fill='x',padx=15,pady=10)

        self.res_title=ctk.CTkLabel(self.result_frame,text='Result',font=('Arial',16,'bold'),text_color='#1A3A6B')
        self.res_title.pack(anchor='w',padx=15,pady=(15,0))

        self.per_lb=ctk.CTkLabel(self.result_frame,text='Percentile',font=('Arial',20,'bold'),text_color='#0B3D91')
        self.per_lb.pack(anchor='w',padx=15,pady=5)

        self.detail_lb=ctk.CTkLabel(self.result_frame,text='',font=('Arial',13),text_color='black',wraplength=550,justify='left')
        self.detail_lb.pack(anchor='w',padx=15,pady=5)

        self.formula_lb=ctk.CTkLabel(self.result_frame,text='Formula Percentile=((Total Students-Your Rank) /Total Students) x 100',
                                   font=('Arial',12),text_color='#444444',wraplength=550,justify='left' )
        self.formula_lb.pack(anchor='w',padx=15,pady=(5,15))

        self.note=ctk.CTkLabel(self,text='Note Rank 1 = 100th percentile. Lower rank is better',font=('Arial',12),text_color='#555555')
        self.note.pack(anchor='w',padx=20,pady=5)
        

    def calculate(self):
        try:
            total=float(self.total_entry.get())
            rank=float(self.rank_entry.get())

            if total<=0 or rank<=0 or rank>total:
                self.per_lb.configure(text='Invalid input')
                return

            perc=((total-rank)/total)*100
            self.per_lb.configure(text=f'Percentile: {perc:.2f}%')
            self.detail_lb.configure(text=f'Your percentile is {perc:.2f}%. you outperformed {perc:.2f}% of the {int(total)} students')

        except Exception as e:
            self.per_lb.configure(text=f'Error: {e}')

        









if __name__=='__main__':
    app=PercentileApp()
    app.mainloop()
