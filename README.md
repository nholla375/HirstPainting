# Hirst Dot Painting Generator

A Python project that uses the `turtle` module to generate a grid of colorful dots inspired by Damien Hirst’s dot paintings. Colors are randomly selected to create a visually pleasing, abstract artwork.

## Features

* Generates a **10×10 grid** of evenly spaced dots
* Randomly selects colors for each dot
* Uses RGB color mode for vibrant colors
* Fast drawing speed with a clean, line-free layout
* Automatically displays artwork until clicked

## How It Works

1. A predefined list of RGB colors is used (extracted from a reference image).
2. The turtle moves in a grid pattern using teleportation to avoid drawing lines.
3. Each position places a dot with a randomly chosen color.
4. The final result is a colorful, abstract dot painting.

## Requirements

* Python 3.x
* `turtle` module (built-in)
* `random` module (built-in)

## Running the Program

```bash
python main.py
```

## Optional Color Extraction

The commented-out section at the top shows how colors can be extracted from an image using the `colorgram` library. This step is optional and not required to run the program.

## Learning Goals

This project was built to practice:

* Nested loops
* Turtle graphics and positioning
* RGB color handling
* Randomization
* Basic generative art techniques
