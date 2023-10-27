    
class Test{

 
    public static void main(String[] args) {

        int[] array1 = {1, 2, 3, 4, 5};

        mystery(array1);

        System.out.println(array1[4]);

    }

    

    public static void mystery(int[] array2) {

        array2[4] = 800;

    }
}