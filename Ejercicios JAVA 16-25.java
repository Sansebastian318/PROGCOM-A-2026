Ejercicios JAVA 16-25

//TABLA DE MULTIPLICACIONES

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el número para la tabla: ");
        int n = sc.nextInt();

        for(int i = 1; i <= 10; i++){
            System.out.println(n + " x " + i + " = " + (n * i));
        }

        sc.close();
    }
}

//Suma de números naturales hasta n

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el valor de n: ");
        int n = sc.nextInt();

        int suma = 0;
        int i = 1;

        while(i <= n){
            suma += i;
            i++;
        }

        System.out.println("La suma es: " + suma);

        sc.close();
    }
}



//Factorial

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese un número: ");
        int n = sc.nextInt();

        if(n < 0){
            System.out.println("No existen factoriales negativos");
        } else {
            int factorial = 1;
            int i = 1;

            while(i <= n){
                factorial *= i;
                i++;
            }

            System.out.println("El factorial es: " + factorial);
        }

        sc.close();
    }
}

//Serie Fibonacci (n números)

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("¿Cuántos números de Fibonacci desea?: ");
        int n = sc.nextInt();

        int a = 0, b = 1;

        for(int i = 0; i < n; i++){
            System.out.println(a);
            int temp = a + b;
            a = b;
            b = temp;
        }

        sc.close();
    }
}


//Adivinar número (10 intentos)

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int numero = 7;
        int intentos = 0;

        while(intentos < 10){
            System.out.print("Adivine el número (0-10): ");
            int intento = sc.nextInt();

            if(intento == numero){
                System.out.println("Correcto!");
                break;
            } else {
                System.out.println("Incorrecto");
            }

            intentos++;
        }

        sc.close();
    }
}

//Números pares del 1 al 100


public class Main {
    public static void main(String[] args) {

        for(int i = 2; i <= 100; i += 2){
            System.out.println(i);
        }
    }
}


//Suma de dígitos

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese un número: ");
        int n = sc.nextInt();
        int suma = 0;

        while(n > 0){
            suma += n % 10;
            n /= 10;
        }

        System.out.println("La suma de los dígitos es: " + suma);

        sc.close();
    }
}


//Número primo

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese un número: ");
        int n = sc.nextInt();
        boolean esPrimo = true;

        if(n <= 1){
            esPrimo = false;
        } else {
            for(int i = 2; i < n; i++){
                if(n % i == 0){
                    esPrimo = false;
                    break;
                }
            }
        }

        if(esPrimo){
            System.out.println("Es primo");
        } else {
            System.out.println("No es primo");
        }

        sc.close();
    }
}


//Triángulo con asteriscos

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Altura del triángulo: ");
        int n = sc.nextInt();

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= i; j++){
                System.out.print("*");
            }
            System.out.println();
        }

        sc.close();
    }
}


//Potencia sin usar **

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Base: ");
        int base = sc.nextInt();

        System.out.print("Exponente: ");
        int exponente = sc.nextInt();

        int resultado = 1;

        for(int i = 0; i < exponente; i++){
            resultado *= base;
        }

        System.out.println("Resultado: " + resultado);

        sc.close();
    }
}