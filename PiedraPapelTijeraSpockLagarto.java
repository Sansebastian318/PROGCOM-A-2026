/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class PiedraPapelTijeraSpockLagarto {
    public static void main(String[] args) {
        System.out.println("Juego: Piedra, Papel, Tijera, Spoke o Lagarto envenenado");
        System.out.println("☢️Debes tener en cuenta estas reglas: Spock rompe tijera, tijera decapita lagarto, tijera corta papel, papel desautoriza Spock, piedra aplasta tijera, papel envuelve piedra, piedra aplasta lagarto, lagarto devora papel, lagarto envenena Spock, Spock vaporiza piedra.");
        System.out.println("1 = Piedra 🪨");
        System.out.println("2 = Papel 📄");
        System.out.println("3 = Tijera ✂️");
        System.out.println("4 = Spock 🖖");
        System.out.println("5 = Lagarto envenenado 🦎");

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        Map<Integer, String> opciones = new HashMap<>();
        opciones.put(1, "Piedra 🪨");
        opciones.put(2, "Papel 📄");
        opciones.put(3, "Tijera ✂️");
        opciones.put(4, "Spock 🖖");
        opciones.put(5, "Lagarto envenenado 🦎");

        while (true) {
            int yo;
            while (true) {
                System.out.print("Elige 1, 2 ,3, 4 o 5: ");
                String input = scanner.nextLine();
                try {
                    yo = Integer.parseInt(input);
                    if (yo < 1 || yo > 5) {
                        System.out.println("❌ Solo puedes elegir 1, 2, 3, 4 o 5.\n");
                        continue;
                    }
                    break;
                } catch (NumberFormatException e) {
                    System.out.println("❌ Debes ingresar un número válido.\n");
                }
            }

            int m = random.nextInt(5) + 1;

            System.out.println("\nTú elegiste: " + opciones.get(yo));
            System.out.println("Máquina eligió: " + opciones.get(m));

            if (yo == m) {
                System.out.println("Empate 🤝");
            } else if ((yo == 1 && (m == 3 || m == 5)) ||(yo == 2 && (m == 1 || m == 4)) ||(yo == 3 && (m == 2 || m == 5)) ||(yo == 4 && (m == 1 || m == 3)) ||(yo == 5 && (m == 2 || m == 4))) {
                System.out.println("¡GANASTE! 🎉");
            } else {
                System.out.println("Perdiste 😢");
            }

            System.out.print("¿Deseas continuar si/no? ");
            String continuar = scanner.nextLine().toLowerCase();
            if (continuar.equals("no")) {
                System.out.println("Gracias por jugar.");
                break;
            }
        }

        scanner.close();
    }
}