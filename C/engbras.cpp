//
// Created by bruno on 09/11/2022.
//

#include "engbras.h"

template <int n> struct vec
{
    float values[n];
};

template <int n> struct mat
{
    float values[n * n];
};

mat<3> Rx(float radians) {
    cout << radians;
}

int main() {
//    mat<3> Ry(float radians); // [0.4]
//    mat<3> Rz(float radians); // [0.4]


    return 0;
}
