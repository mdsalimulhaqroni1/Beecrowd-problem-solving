
A, B, C = map(float, input().split())

triangle_area = (A * C) / 2

circle_area = 3.14159 * (C ** 2)

trapezium_area = ((A + B) * C) / 2

square_area = B ** 2

rectangle_area = A * B
print("TRIANGULO:", format(triangle_area, ".3f"))
print("CIRCULO:", format(circle_area, ".3f"))
print("TRAPEZIO:", format(trapezium_area, ".3f"))
print("QUADRADO:", format(square_area, ".3f"))
print("RETANGULO:", format(rectangle_area, ".3f"))