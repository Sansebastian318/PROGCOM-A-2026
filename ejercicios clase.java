/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        double suma = 0;
        int c = 0;
        ArrayList<Double> notas = new ArrayList<>();
        int n = 10;
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < n; i++) {
            System.out.print("Ingrese la nota del estudiante " + (i + 1) + ": ");
            double nota = scanner.nextDouble();
            notas.add(nota);
            suma += nota;
        }

        double prom = suma / n;
        System.out.printf("\nPromedio del curso: %.2f\n", prom);
        System.out.println("\nEstudiantes con nota mayor al promedio:");

        for (int i = 0; i < n; i++) {
            if (notas.get(i) > prom) {
                c++;
                System.out.println(" - Estudiante " + (i + 1) + ": " + notas.get(i));
            }
        }

        System.out.println("\nTotal: " + c + " estudiantes sacaron mas que el promedio");

        double nota_max = notas.get(0);
        int indice_max = 0;
        for (int i = 1; i < n; i++) {
            if (notas.get(i) > nota_max) {
                nota_max = notas.get(i);
                indice_max = i;
            }
        }

        System.out.println("\nEl estudiante con mayor nota fue el estudiante " + (indice_max + 1) + " con " + nota_max);
        scanner.close();
    }
}