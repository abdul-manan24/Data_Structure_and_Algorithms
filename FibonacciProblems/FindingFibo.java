package FibonacciProblems;
public class FindingFibo {
    
    public static int f(int n) {
        if (n <= 1) {
            return n;
        }
        else
        {
            return f(n-1) + f(n-2);
        }
    }
    public static void main(String[] args) {
        int nthNumber = f(4);
        System.out.print(nthNumber);   
    }
}
