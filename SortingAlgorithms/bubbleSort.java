package SortingAlgorithms;
public class bubbleSort {
    public static void main(String[] args) {

        int[] myNumbers = {7, 9, 11, 12, 3};
        
        for (int i=0; i < myNumbers.length - 1; i++) {
            boolean swapped = false;
            for (int j=0; j < myNumbers.length - 1 - i; j++) {
                if (myNumbers[j] > myNumbers[j+1]) {
                    int temp = myNumbers[j];
                    myNumbers[j] = myNumbers[j+1];
                    myNumbers[j+1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
        }

        System.out.print("Sorted array: ");
        for (int k=0; k<myNumbers.length; k++) {
            System.out.print(myNumbers[k] + " ");
        }
    }
}
