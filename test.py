"""
    Author: i_dovelemon[1322600812@qq.com]
    Date: 2018/02/18
    Brief: Test the Discrete Fourier Transform algorithm
"""

import random
import tkinter
import discrete_fourier_transform

SAMPLER_NUM = 64
SAMPLER_WIDTH = 15
POINT_WIDTH = 4

def generate_random_signals(number):
    signals = []
    for i in range(number):
        signals.append(random.randint(0, 256))

    return tuple(signals)

if __name__ == "__main__":
    # Generate random signals
    signals = generate_random_signals(SAMPLER_NUM)

    # Analysis random signals
    reals, images = discrete_fourier_transform.dft_real_analysis_correlation(SAMPLER_NUM, signals)

    # Synthesis random signals
    signals_after_synthesis = discrete_fourier_transform.dft_real_synthesis(SAMPLER_NUM, reals, images)

    # Draw

    # Orignal signals
    tk = tkinter.Tk()
    canvas0 = tkinter.Canvas(tk, width = (SAMPLER_NUM - 1) * SAMPLER_WIDTH, height = 300, bg = "black")
    canvas0.pack()

    canvas0.create_text(80, 280, text= "Orignal Signals", font = "time 10 bold", tags = "string", fill = "white")

    for i in range(SAMPLER_NUM):
        canvas0.create_line(i * SAMPLER_WIDTH - POINT_WIDTH, signals[i], i * SAMPLER_WIDTH + POINT_WIDTH, signals[i], width = POINT_WIDTH * 2, fill = "white")

    for i in range(SAMPLER_NUM - 1):
        canvas0.create_line(i * SAMPLER_WIDTH, signals[i], (i + 1) * SAMPLER_WIDTH, signals[i + 1], fill = "red")

    # Synthesis signals
    canvas1 = tkinter.Canvas(tk, width = (SAMPLER_NUM - 1) * SAMPLER_WIDTH, height = 300, bg = "#111111")
    canvas1.pack()

    canvas1.create_text(80, 280, text= "Synthesis Signals", font = "time 10 bold", tags = "string", fill = "white")

    for i in range(SAMPLER_NUM):
        canvas1.create_line(i * SAMPLER_WIDTH - POINT_WIDTH, signals_after_synthesis[i], i * SAMPLER_WIDTH + POINT_WIDTH, signals_after_synthesis[i], width = POINT_WIDTH * 2, fill = "white")

    for i in range(SAMPLER_NUM - 1):
        canvas1.create_line(i * SAMPLER_WIDTH, signals_after_synthesis[i], (i + 1) * SAMPLER_WIDTH, signals_after_synthesis[i + 1], fill = "red")    

    tk.mainloop()