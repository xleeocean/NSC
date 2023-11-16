
/**
 * A program that calls functions to do console-based plotting of curves/lines
 * in quadrants I and II, but sideways.
 * While each function calculate y as below:
 * - plotXSquared: y = x*x
 * - plotNegXSquaredPlus20: y = |x|+1
 * - plotAbsXPlus1: y = -(x*x)+20
 * - plotSinWave: y = 20sin(.5x)+20
 *
 * @author: Alice Li
 * @date: 10/18/2023
 */

public class SidePlot{
    // Global variables
    static String PLOT_CHAR = "o";
    static int minX;
    static int maxX;

    // Main function to call other functions by arguments
    public static void main(String args[]) {
        plotXSquared(-6,6);
        plotAbsXPlus1(-5,5);
        plotNegXSquaredPlus20(-4,4);
        plotSinWave(-9,9);
    }

    // Plot where y = x*x
    public static void plotXSquared(int minX, int maxX) {
        System.out.println("Sideways Plot");
        System.out.println("y = x*x where "+ minX + "<=x<=" + maxX);
        for(int x = minX; x <= maxX; x++) {
            int y = x*x + 2;
            if(x == 0) {
                for(int len = 0; len <= maxX*maxX + 2; len++) {
                    if (len == y) {
                    System.out.print(PLOT_CHAR);
                    } else if (len == 2){
                        System.out.print("+");
                    } else {
                        System.out.print("-");
                    }
                }
            }
            else{
                for(int len = 0; len <= y+3; len++) {
                    if (len == y) {
                        System.out.print(PLOT_CHAR);
                    } else if (len == 2){
                        System.out.print("|");
                    } else {
                        System.out.print(" ");
                    }
                }
            }
            System.out.println();
        }
        System.out.println("");
    }

    // Plot where y = |x|+1
    public static void plotAbsXPlus1(int minX, int maxX) {
        System.out.println("Sideways Plot");
        System.out.println("y = |x|+1, where "+ minX + "<=x<=" + maxX);
        for(int x = minX; x <= maxX; x++) {
            int y = Math.abs(x) + 3;
            if(x == 0) {
                for(int len = 0; len <= Math.abs(maxX) + 3; len++) {
                    if (len == y) {
                    System.out.print(PLOT_CHAR);
                    } else if (len == 2){
                        System.out.print("+");
                    } else {
                        System.out.print("-");
                    }
                }
            }
            else{
                for(int len = 0; len <= y+3; len++) {
                    if (len == y) {
                        System.out.print(PLOT_CHAR);
                    } else if (len == 2){
                        System.out.print("|");
                    } else {
                        System.out.print(" ");
                    }
                }
            }
            System.out.println();
        }
        System.out.println("");
    }

    // Plot where y = -(x*x)+20
    public static void plotNegXSquaredPlus20(int minX, int maxX) {
        System.out.println("Sideways Plot");
        System.out.println("y = -(x*x)+20, where "+ minX + "<=x<=" + maxX);
        for(int x = minX; x <= maxX; x++) {
            int y = -(x*x) + 22;
            if(x == 0) {
                for(int len = 0; len <= 23; len++) {
                    if (len == y) {
                    System.out.print(PLOT_CHAR);
                    } else if (len == 2){
                        System.out.print("+");
                    } else {
                        System.out.print("-");
                    }
                }
            }
            else{
                for(int len = 0; len <= y+3; len++) {
                    if (len == y) {
                        System.out.print(PLOT_CHAR);
                    } else if (len == 2){
                        System.out.print("|");
                    } else {
                        System.out.print(" ");
                    }
                }
            }
            System.out.println();
        }
        System.out.println("");
    }

    // Plot where y = 20sin(.5x)+20
    public static void plotSinWave(int minX, int maxX) {
        System.out.println("Sideways Plot");
        System.out.println("y = 20sin(.5x)+20 where "+ minX + "<=x<=" + maxX);
        for(int x = minX; x <= maxX; x++) {
            int y = (int)(20 * Math.sin(0.5 * x) + 22);
            if(x == 0) {
                for(int len = 0; len <= 20*1+22; len++) {
                    if (len == y) {
                    System.out.print(PLOT_CHAR);
                    } else if (len == 2){
                        System.out.print("+");
                    } else {
                        System.out.print("-");
                    }
                }
            }
            else{
                for(int len = 0; len <= 20*1+22; len++) {
                    if (len == y) {
                        System.out.print(PLOT_CHAR);
                    } else if (len == 2){
                        System.out.print("|");
                    } else {
                        System.out.print(" ");
                    }
                }
            }
            System.out.println();
        }
        System.out.println("");
    }
}

