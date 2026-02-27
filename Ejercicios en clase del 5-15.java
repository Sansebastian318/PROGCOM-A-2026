Ejercicio Función cuadrática.

import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        double d = b*b - 4*a*c;

        if(d > 0){
            double x1 = (-b + Math.sqrt(d))/(2*a);
            double x2 = (-b - Math.sqrt(d))/(2*a);
            System.out.println("Dos soluciones: " + x1 + " y " + x2);
        } 
        else if(d == 0){
            double x = -b/(2*a);
            System.out.println("Una solución: " + x);
        } 
        else {
            System.out.println("No tiene soluciones reales");
        }

    }
}

Ejercicio PAR O IMPAR
import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

int n = sc.nextInt();
System.out.println(n % 2 == 0 ? "Par" : "Impar");
        }

    }

Ejercicio Año Bisiesto

import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

int a = sc.nextInt();

if((a%4==0 && a%100!=0) || (a%400==0))
    System.out.println("Bisiesto");
else
    System.out.println("No bisiesto");
        }

    }

Prioridad tercera edad

import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

String nombre = sc.next();
int edad = sc.nextInt();

System.out.println(edad >= 70 ? "Tiene prioridad" : "No tiene prioridad");

    }
}


Mayor de tres números

import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt();

if(a>b && a>c)
    System.out.println("Mayor: "+a);
else if(b>c)
    System.out.println("Mayor: "+b);
else
    System.out.println("Mayor: "+c);

    }
}

Tipo de triángulo

import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt();

if(a==b && b==c)
    System.out.println("Equilátero");
else if(a==b || b==c || a==c)
    System.out.println("Isósceles");
else
    System.out.println("Escaleno");

    }
}

Ejercicio IMC


import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

String nombre=sc.next();
double peso=sc.nextDouble();
double altura=sc.nextDouble();

double imc=peso/(altura*altura);
String cat;
String desc;

if(imc<18.5){
    cat="Bajo peso";
    desc="Debe mejorar su alimentación.";
}
else if(imc<25){
    cat="Normal";
    desc="Debe mantener hábitos saludables.";
}
else if(imc<30){
    cat="Sobrepeso";
    desc="Debe hacer más ejercicio y cuidar su dieta.";
}
else{
    cat="Obesidad";
    desc="Debe acudir a un especialista.";
}

System.out.println(nombre+" "+cat);
System.out.println("Recomendación: "+desc);
    }
}

Calculadora simple

double a=sc.nextDouble();
double b=sc.nextDouble();
char op=sc.next().charAt(0);

if(op=='+') System.out.println(a+b);
else if(op=='-') System.out.println(a-b);
else if(op=='*') System.out.println(a*b);
else if(op=='/') System.out.println(b!=0 ? a/b : "Error");


Calificación en letras

int n=sc.nextInt();

if(n>=90) System.out.println("A");
else if(n>=80) System.out.println("B");
else if(n>=70) System.out.println("C");
else if(n>=60) System.out.println("D");
else System.out.println("F");


Día de la semana según el número digitado

import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

int d=sc.nextInt();

String dia = (d==1)?"Lunes":
             (d==2)?"Martes":
             (d==3)?"Miércoles":
             (d==4)?"Jueves":
             (d==5)?"Viernes":
             (d==6)?"Sábado":
             (d==7)?"Domingo":"Inválido";

System.out.println(dia);
    }
}

Ejercicio triángulo

import java.util.Scanner;
import java.math.BigDecimal;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        BigDecimal a = new BigDecimal(sc.next());
        BigDecimal b = new BigDecimal(sc.next());
        BigDecimal c = new BigDecimal(sc.next());

        if(a.compareTo(BigDecimal.ZERO) > 0 &&
           b.compareTo(BigDecimal.ZERO) > 0 &&
           c.compareTo(BigDecimal.ZERO) > 0){

            if(a.add(b).compareTo(c) > 0 &&
               a.add(c).compareTo(b) > 0 &&
               b.add(c).compareTo(a) > 0){

                String tipo;

                if(a.equals(b) && b.equals(c))
                    tipo="Equilátero";
                else if(a.equals(b) || b.equals(c) || a.equals(c))
                    tipo="Isósceles";
                else
                    tipo="Escaleno";

                System.out.println("Sí se puede formar un triángulo.");
                System.out.println("Tipo de triángulo: " + tipo);

            } else {
                System.out.println("No se puede formar un triángulo.");
            }

        } else {
            System.out.println("Los valores deben ser mayores que 0.");
        }

    }
}




