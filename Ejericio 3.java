/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] productos = {"Combo1","Combo2","Combo3","Combo4","Papas","Jugo","Cerveza","Agua","Gaseosa"};
        int[] precios = {20000,25000,18000,24500,3000,7000,3500,4000,2500};
        int total = 0;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Cantidad de clientes: ");
        int n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.println("1 Combo1");
            System.out.println("2 Combo2");
            System.out.println("3 Combo3");
            System.out.println("4 Combo4");
            System.out.println("5 Papas");
            System.out.println("6 Jugo");
            System.out.println("7 Cerveza");
            System.out.println("8 Agua");
            System.out.println("9 Gaseosa");

            System.out.print("Que desea ordenar, ingrese el número antes del combo, ejemplo: digito el numero 1: ");
            int opcion = scanner.nextInt();

            total += precios[opcion - 1];
        }

        System.out.println("Dinero recaudado en el dia: " + total);
        scanner.close();
    }
}