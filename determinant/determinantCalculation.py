import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):        
        frame = tk.Frame.__init__(self, parent)
        frame2 = tk.Frame.__init__(self, parent)

        self.frame2.pack(side="right", pady=15, padx=10)

        # create a canvas and parameters
        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.pointscoords = []
        
        
        # Buttons to add new Dots to the canvas and delete them
        self.animateButton = tk.Button(frame, text="Animate", 
                                     relief="raised",
                                     command = lambda: self.move())
        self.animateButton.config(height = 2, width = 10 )
        self.animateButton.place(x=5, y=5)
        self.animateButton.state = True
        
        self.deleteButton = tk.Button(frame, text="Delete", 
                                     relief="raised",
                                     )
        
        self.deleteButton.config( height = 2, width = 10 )
        self.deleteButton.place(x=5, y=50)
        self.deleteButton.state = True




        # on mouse click create a point
       # self.canvas.bind("", lambda event: self.createPoint(event.x, event.y))
        




if __name__ == "__main__":
    
    #create a window and set parameters of a window
    root = tk.Tk()
    width = 800
    height = 600
    
    #center it    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - width / 2)
    center_y = int(screen_height/2 - height*6/10)
        
    root.geometry(f'{width}x{height}+{center_x}+{center_y}')
    root.title('Bezier Curve Algorithm')
   
        
    Example(root).pack( fill = 'both' , expand = False)
    
    root.mainloop()