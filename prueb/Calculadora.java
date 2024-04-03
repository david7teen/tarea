import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa el primer número: ");
        double num1 = scanner.nextDouble();
        
        System.out.print("Ingresa el segundo número: ");
        double num2 = scanner.nextDouble();
        
        System.out.println("Selecciona una operación:");
        System.out.println("1. Sumar");
        System.out.println("2. Restar");
        System.out.println("3. Multiplicar");
        System.out.println("4. Dividir");
        System.out.println("5. indicar si la palabra ingresada es Palíndrome");
        
        int opcion = scanner.nextInt();
        double resultado = 0;
        scanner.close();
        switch (opcion) {
            case 1:
            resultado = sumar(num1, num2);
            break;
        case 2:
            resultado = restar(num1, num2);
            break;
        case 3:
            resultado = multiplicar(num1, num2);
            break;
        case 4:
            resultado = dividir(num1, num2);
            break;
            case 5:
                String palabra="ala";
                String Inver;
                Inver = (inverPalabra(palabra, palabra.length()-1));
                System.out.println(Inver);
                System.out.println(palabra);
                if(palabra==Inver){
                    System.out.println("las palabras son iguales");
        
                }else{
                    System.out.println("las palabras no son iguales");
                }
            default:
                System.out.println("Opción inválida.");
                return;
        }
        
        System.out.println("El resultado es: " + resultado);
        
    }
    
    public static double sumar(double a, double b) {
        return a + b;
    }
    
    public static double restar(double a, double b) {
        return a - b;
    }
    
    public static double multiplicar(double a, double b) {
        return a * b;
    }
    
    public static double dividir(double a, double b) {
        if (b != 0) {
            return a / b;
        } else {
            throw new ArithmeticException("No se puede dividir por cero.");
        }
    }
    public static String inverPalabra(String palabra, int longitud){


        if (longitud==0){
            return palabra.charAt(longitud)+"";
        }else {
            return (palabra.charAt(longitud) + (inverPalabra(palabra, longitud-1)));
        }
    }

}