package FibonacciProblems;
// This is a for loop approach to print 13 first fibonacci terms. 

public class Fibonacci{

    public static void main(String[] args) {
        int first = 0;
        int second = 1;

        for (int i=0; i<=12; i++) {
            int nextFiboNum = first + second;

            System.out.println(first);

            first = second;
            second = nextFiboNum;
        }
    }
}