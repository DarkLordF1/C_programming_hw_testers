#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
    int num = 0, reversedNum = 0, last_digit = 0;  // Declare and initialize variables
    scanf("%d", &num);  // Read an integer input from the user

    // Loop to reverse the number
    while (num != 0) {
        last_digit = num % 10;  // Get the last digit
        reversedNum = (reversedNum *10  + last_digit);  // Shift digits left and add the last digit
        num /= 10;  // Remove the last digit from num
    }

    // Print the reversed number
    printf("Reverse of number is: %d\n", reversedNum);

    return 0;  // Exit successfully
}
