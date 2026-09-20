package SortingAlgorithms;
public class selectionSort {
    public static void main(String[] args) {

        int[] myNumbers = {6, 2, 1, 25, 3, 4, 2};

        for (int i=0; i<myNumbers.length; i++) {
            int minIndex = i;
            for (int j=i + 1; j<myNumbers.length; j++) {
                if (myNumbers[j] < myNumbers[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = myNumbers[i];
            myNumbers[i] = myNumbers[minIndex];
            myNumbers[minIndex] = temp;
        }

        System.out.print("Sorted list" + " ");
        for (int k=0; k<myNumbers.length; k++) {
            System.out.print(myNumbers[k] + " ");
        }
    }
}

// Improvement needed this algorithem is buggy