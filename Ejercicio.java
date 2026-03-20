/**************************
temp=float(input("temperatura registrada"))
if temp>=27: print("pongase algo fresco")
elif temp>-20 and temp<27: print("abrigate")
elif temp>16 and temp<20: print("abrigate mas")
else: print("esta helando")

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		System.out.println("Temperatura registrada:");
		Scanner leer = new Scanner(System.in);
		//nextline es para string
		//nextFloat es para leer decimales
		float temp = leer.nextFloat();
		//&& and || or
		if (temp>=27){System.out.println("Póngase algo fesco");}
		else if (temp>=20 && temp<27){System.out.println("Abrigate");}
		else if (temp>16 && temp<20){System.out.println("abrigate mas");}
		else {System.out.println("esta helando");}
		
		//Ejercicio para easy hand if
		System.out.println("Cuál es tu edad");
		int edad = leer.nextInt();
		System.out.println(edad>=18? "Eres mayor de edad":"No eres mayor de edad");
		
	
	}	   
}