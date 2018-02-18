"""
    Author: i_dovelemon[1322600812@qq.com]
    Date: 2018/02/12
    Brief: Algorithm for Discrete Fourier Transform
"""

import math

__all__ = ["dft_real_synthesis", "dft_real_analysis_correlation", "dft_real_analysis_fft"]

#---------------------------------------------------------------
# Real number Discrete Fourier Transform algorithm

def dft_real_synthesis(number, reals, images):
    """ Synthesis time domain signal

    According to frequency domain real part and image part data to synthesis a time domain signal

    Args:
        number: The length of the time domain signal samplers
        reals: The real part data of frequency domain signal samplers(for cos wave)
        images: The image part data of frequency domain signal samplers(for sin wave)

    Returns:
        A array hold all time domain signal samplers
    """
    # Check parameters
    if number % 2 != 0:
        raise Exception("Invalid parameter: number, must be an even number", number)

    halfNumber = int(number / 2)
    frequencyNumber = halfNumber + 1

    if len(reals) != frequencyNumber:
        raise Exception("Invalid parameter: reals, check the length of the reals")

    if len(images) != frequencyNumber:
        raise Exception("Invalid parameter: image, check the length of the images")

    # Convert to amplitude
    amplitudeReals = []
    amplitudeImages = []
    for k in range(frequencyNumber):
        # Real part data's first and last element need special work
        if k == 0 or k == halfNumber:
            amplitudeReals.append(1.0 * reals[k] / number)
        else:
            amplitudeReals.append(1.0 * reals[k] / halfNumber)

        amplitudeImages.append(-1.0 * images[k] / halfNumber)

    # Synthesis to time domain signal
    result = []
    for i in range(number):
        real = 0.0
        for k in range(frequencyNumber):
            real = real + amplitudeReals[k] * math.cos(2.0 * 3.14159 * k * i / number)
        
        image = 0.0
        for k in range(frequencyNumber):
            image = image + amplitudeImages[k] * math.sin(2.0 * 3.14159 * k * i / number)

        result.append(real + image)

    return tuple(result)

def dft_real_analysis_correlation(number, signals):
    """ Analysis the Discrete Fourier Transform signal using correlation method

    Analysis frequency domain signal real part and image part signal data according to the input time domain Discrete Fourier Transform signals

    Args:
        number: The length of the time domain signal samplers
        signals: The time domain signals

    Returns:
        Two tuple hold frequency domain real and image part data
    """
    # Check parameters
    if number % 2 != 0:
        raise Exception("Invalid parameters:number", number)

    if len(signals) != number:
        raise Exception("Invalid parameter, check the length of the signals")

    # Correlation
    reals = []
    images = []
    
    frequencyNum = int(number / 2 + 1)

    for k in range(frequencyNum):
        real = 0.0
        image = 0.0

        for i in range(number):
            real = real + signals[i] * math.cos(2.0 * 3.14159 * k * i / number)
            image = image + signals[i] * math.sin(2.0 * 3.14159 * k * i / number)

        reals.append(real)

        # Image part data's first and last element do not affect the final result, set it 0
        if k == 0 or k == frequencyNum - 1:
            images.append(0.0)
        else:
            images.append(-image)
    
    return tuple(reals), tuple(images)

def dft_real_analysis_fft():
    pass

#---------------------------------------------------------------
# Complex number Discrete Fourier Transform algorithm


if __name__ == "__main__":
    number = 4
    reals = (1, 2, 3)
    images = (0, 2, 0)
    time = dft_real_synthesis(number, reals, images)
    frequencyReals, frequencyImages = dft_real_analysis_correlation(number, time)