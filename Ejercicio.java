/******************************************************************************

import java.util.*;
public class Main
{
	public static void main(String[] args) {
		System.out.println("Temperatura registrada:");
		Scanner leer = new Scanner(System.in);
		//nextline es para string
		//nextFloat es para leer decimales
		float temp = leer.nextFloat();
		
		if (temp>=27){System.out.println("pongase algo fresco");}
		else if (temp>=20 && temp<27){System.out.println("abrígate");}
	    else if (temp >= 16 && temp < 20) {
            System.out.println("abrígate más");
        } else {
            System.out.println("Está helando");
        }
	}
}
*******************************************************************************/
System.out.println("Cual es tu edad?")
int edad = leer.nextInt();
System.out.println(edad>=18? "Eres mayor de edad: ":"No eres mayor de edad");