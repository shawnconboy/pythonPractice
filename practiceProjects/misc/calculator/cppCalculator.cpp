#include <iostream>
using namespace std;

void clearScreen() {
  system("clear");
}

void header() {
  cout << "Calculator" << endl;
  cout << "---------------------------------------------" << endl;
  cout << endl;
}

int main() {
  clearScreen();
  header();

  cout << "What would you like to do?" << endl;

  cout << "\n1. Add" << endl;
  cout << "2. Subtract" << endl;
  cout << "3. Multiply" << endl;
  cout << "4. Divide" << endl;

  int userChoice;
  cout << "\nPlease make a selection : ";
  cin >> userChoice;

  if (userChoice == 1) {
    clearScreen();
    header();
    cout << "Addition" << endl;
    cout << "----------------------" << endl;

    int num1, num2, total;
    cout << "\nEnter number : ";
    cin >> num1;
    cout << "Enter number to add : ";
    cin >> num2;

    total = num1 + num2;
    cout << "\n" << num1 << " + " << num2 << " = " << total << endl;
  } else if (userChoice == 2) {
    clearScreen();
    header();
    cout << "Subtraction" << endl;
    cout << "----------------------" << endl;

    int num1, num2, total;
    cout << "\nEnter number : ";
    cin >> num1;
    cout << "Enter number to subtract : ";
    cin >> num2;

    total = num1 - num2;
    cout << "\n" << num1 << " - " << num2 << " = " << total << endl;
  } else if (userChoice == 3) {
    clearScreen();
    header();
    cout << "Multplication" << endl;
    cout << "----------------------" << endl;

    int num1, num2, total;
    cout << "\nEnter number : ";
    cin >> num1;
    cout << "Enter number to multiply : ";
    cin >> num2;

    total = num1 * num2;
    cout << "\n" << num1 << " * " << num2 << " = " << total << endl;
  } else if (userChoice == 4) {
    clearScreen();
    header();
    cout << "Divsion" << endl;
    cout << "----------------------" << endl;

    int num1, num2;
    double total;
    cout << "\nEnter number : ";
    cin >> num1;
    cout << "Enter number to divide : ";
    cin >> num2;

    total = static_cast<double>(num1) / num2;
    cout << "\n" << num1 << " / " << num2 << " = " << total << endl;
  }

  return 0;
}
