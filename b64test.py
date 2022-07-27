import tkinter as tk

IMAGE_DATA = '''
    R0lGODlhEAAQALMAAAAAAP//AP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAA\nAAAAACH5BAEAAAIALAAAAAAQABAAQAQ3UMgpAKC4hm13uJnWgR
    TgceZJllw4pd2Xpagq0WfeYrD7\n2i5Yb+aJyVhFHAmnazE/z4tlSq0KIgA7\n
    '''

root = tk.Tk()
image = tk.PhotoImage(data=IMAGE_DATA)
label = tk.Label(root, image=image, padx=20, pady=20)
label.pack()

root.mainloop()