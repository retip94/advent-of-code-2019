class Image:
    def __init__(self, width, height):
        self.encoded_image = open("input.txt", "r").read()
        self.width = width
        self.height = height
        self.layers = []
        self.__createLayers()
        self.final_image = []

    def __createLayers(self):
        layers_number = len(self.encoded_image) / (self.width * self.height)
        for i in range(0, int(layers_number)):
            layer = []
            try:
                for y in range(0, self.height):
                    row = []
                    for x in range(0, self.width):
                        row.append(int(self.encoded_image[i * self.width * self.height + y * self.width + x]))
                    layer.append(row)
            except IndexError:
                print("fail")
            self.layers.append(layer)

    def __find_layers_with_fewest_zeros(self):
        min_zeros = 99999999999999999999999999999
        layer_with_fewest = None
        for layer in self.layers:
            zeros = self.__count_single_digit(layer, 0)
            if zeros < min_zeros:
                min_zeros = zeros
                layer_with_fewest = layer
        return layer_with_fewest

    def __count_single_digit(self, layer, digit):
        counter = 0
        for row in layer:
            for pixel in row:
                if int(pixel) == digit:
                    counter += 1
        return counter

    def get_part_one_result(self):
        layer = self.__find_layers_with_fewest_zeros()
        ones = self.__count_single_digit(layer, 1)
        twos = self.__count_single_digit(layer, 2)
        return ones * twos

    def merge_layers(self):
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                final_pixel = 2
                for layer in self.layers:
                    final_pixel = layer[y][x]
                    if final_pixel in [0, 1]:
                        break
                row.append(final_pixel)
            self.final_image.append(row)
        return self.final_image

    def __repr__(self):
        image_string = ""
        for row in self.final_image:
            for pixel in row:
                if int(pixel) == 0:
                    image_string += 'x'
                else:
                    image_string += ' '
            image_string += '\n'
        return image_string


image = Image(25,6)
print("answer for part1 is: ", image.get_part_one_result())
image.merge_layers()
print(image)
