#include <stdio.h>
#include "Python.h"

int func(int num_numbers, int *numbers)
{
    int i;
    int sum = 0;
    for (i = 0; i < num_numbers; i++)
    {
        sum += numbers[i];
    }
    return sum;
}
