/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int votos[] = new int[5];

        System.out.print("Cuántos votantes: ");
        int n = sc.nextInt();

        for(int i = 0; i < n; i++){
            System.out.print("Vote por candidato (1-5): ");
            int voto = sc.nextInt();
            votos[voto-1] = votos[voto-1] + 1;
        }

        for(int i = 0; i < 5; i++){
            System.out.println("Candidato " + (i+1) + ": " + votos[i]);
        }

        int mayor1 = 0, mayor2 = 0;
        int pos1 = 0, pos2 = 0;

        for(int i = 0; i < 5; i++){
            if(votos[i] > mayor1){
                mayor2 = mayor1;
                pos2 = pos1;

                mayor1 = votos[i];
                pos1 = i;
            }
            else if(votos[i] > mayor2){
                mayor2 = votos[i];
                pos2 = i;
            }
        }

        System.out.println("Segunda vuelta: " + (pos1+1) + " y " + (pos2+1));

        int v1 = 0, v2 = 0;

        for(int i = 0; i < n; i++){
            System.out.print("Vote 1 o 2: ");
            int voto = sc.nextInt();

            if(voto == 1){
                v1++;
            }else{
                v2++;
            }
        }

        if(v1 > v2){
            System.out.println("Ganador candidato " + (pos1+1));
        }else{
            System.out.println("Ganador candidato " + (pos2+1));
        }

    }
