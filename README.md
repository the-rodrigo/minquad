# Calculadora de Mínimos Quadrados

## About

The project is a calculator of the Least Square Method using a collection of points xi, yi. With the pourpose of linearization the values in a line equation.

## Methodology

The angular coefficient was calculated using the formula:<br>
<img src="https://github.com/the-rodrigo/minquad/blob/main/assets/Coeficiente-Angular.PNG"></img><br>

The linear coefficient was calculated using the formula:<br>
<img src="https://github.com/the-rodrigo/minquad/blob/main/assets/Coefiente-Linear.PNG"></img><br>

The linear correlation coefficient was calculated using the formula:<br>
<img src="https://github.com/the-rodrigo/minquad/blob/main/assets/Coeficiente-de-Correlacao.png"></img><br>

## How to use

#### Import the module
- from minquad import main

#### 🧠 <strong>minquad function</strong>
- Parameters: xi, yi -> Two lists with the collection of points xi and yi<br>
- Exits: angular, linear, r2 -> Angular, linear and linear correlation coefficients
