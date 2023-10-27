import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class App {

    // Function to read a file and store its lines in an ArrayList
    public static ArrayList<String> readFileToArrayList(String filePath) {
        ArrayList<String> arrayList = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                arrayList.add(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return arrayList;
    }

    // Function to create and return an ArrayList of words read from a file
    public static ArrayList<String> creatarraylist() {
        // Replace "path/to/your/file.txt" with the actual path to your text file.
        String filePath = "c:\\Users\\billa\\Documents\\onq.queensu.ca_content_enforced_772129-CISC124(ASO)S23_wordlist.txt_ou=772129.txt";
        ArrayList<String> linesList = readFileToArrayList(filePath);

        // Display the content of the ArrayList
        return linesList;
    }

    // Lists of consonants and vowels
    public static String[] initallistofconstants = { "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w","x", "y", "z"};
    public static String[] initallistofvowels = { "a", "e", "i", "o", "u" };

    // Function to generate a random vowel or consonant
    public static String ranlet(String[] listv, int upper) {
        Random rand = new Random();
        int int_random_index = rand.nextInt(upper);

        return listv[int_random_index];
    }

    // Function to generate an array of random consonants and vowels
    public static String[] genrandom() {
        String chosenvowels[] = new String[3];
        String chosenconstants[] = new String[8];
        String[] listofvowels = initallistofvowels;
        String[] listofconstants = initallistofconstants;

        // Randomly select 3 vowels
        for (int i = 0; i < 3; i++) {
            String targetv = ranlet(listofvowels, listofvowels.length - 1);
            String[] buffer = new String[listofvowels.length - 1];

            // Remove the selected vowel from the list of vowels
            for (int p = 0, k = 0; p < listofvowels.length || k < buffer.length; p++)
                if (listofvowels[p] != targetv) {
                    buffer[k] = listofvowels[p];
                    k++;
                } else
                    continue;

            listofvowels = buffer;
            chosenvowels[i] = targetv;
        }

        // Randomly select 8 consonants
        for (int i = 0; i < 8; i++) {
            String target = ranlet(listofconstants, listofconstants.length - 1);
            String[] buffer = new String[listofconstants.length - 1];

            // Remove the selected consonant from the list of consonants
            for (int p = 0, k = 0; p < listofconstants.length || k < buffer.length; p++)
                if (listofconstants[p] != target) {
                    buffer[k] = listofconstants[p];
                    k++;
                } else
                    continue;

            listofconstants = buffer;
            chosenconstants[i] = target;
        }

        // Combine the selected consonants and vowels into a single array
        String[] listofletters = new String[chosenconstants.length + chosenvowels.length];
        System.arraycopy(chosenconstants, 0, listofletters, 0, chosenconstants.length);
        System.arraycopy(chosenvowels, 0, listofletters, chosenconstants.length, chosenvowels.length);

        return listofletters;
    }

    // Function to check if all letters in a word are present in a reference array
    public static boolean correct_lettercheck(String[] word, String[] reference) {
        int flase = 0;
        for (int z = 0; z < word.length; z++) {
            int flag = 0;
            for (int k = 0; k < reference.length; k++) {
                if (word[z] == reference[k])
                    flag++;
            }
            if (flag >= reference.length) {
                flase++;
            } else
                continue;
        }
        if (flase != 0)
            return false;
        else
            return true;
    }

    // Function to check if a given input is a word in the list of words
    public static boolean is_a_wordcheck(String input) {
        ArrayList<String> mitlist = creatarraylist();
        if (mitlist.contains(input)) {
            return true;
        } else
            return false;
    }

    // Function to play the game, taking user input and calculating points
    public static int play(String name1, String keyword) {
        ArrayList<String> guessed = new ArrayList<String>();
        String[] x = genrandom();

        System.out.println(name1 + " here are your letters: \n" + Arrays.toString(x));

        String userName;
        int points = 0;
        boolean running = true;

        while (running) {
            Scanner guess = new Scanner(System.in);
            // Enter username and press Enter
            System.out.println("Enter guess");
            userName = guess.nextLine().toLowerCase();

            // Check if the user entered the keyword to end the game
            if (userName.equals(keyword)) {
                System.out.println("Your total points are:" + points);
                running = false;
                break;
            }

            String[] splitword = userName.split("");

            // Check if the user's guess is valid, and if it's a word in the list
            if (correct_lettercheck(splitword, x) && is_a_wordcheck(userName)) {
                if (guessed.contains(userName)) {
                    System.out.println("Invalid Guess Try again");
                } else {
                    guessed.add(userName);
                    System.out.println(" Good guess");
                    points += userName.length();
                    System.out.println("Your total points are:" + points);
                }
            } else {
                System.out.println("Invalid Guess Try again");
            }
        }

        return points;
    }
    public static void main(String[] tesr) {
        // Create two Scanner objects to read player names
        Scanner player1 = new Scanner(System.in);
        Scanner player2 = new Scanner(System.in);
    
        // Prompt for and read player names
        System.out.println("Enter player one name");
        String name1 = player1.nextLine();
    
        System.out.println("Enter player two name");
        String name2 = player2.nextLine();
    
        // Display welcome message
        System.out.println("WELCOME " + name1 + " and " + name2 + "!!!");
    
        // Start the game with player 1 going first
        System.out.println(name1 + " GOES FIRST(ENTER DONE ONCE COMPLETE)");
    
        // Get the score for player 1
        int player1Score = play(name1, "done");
        System.out.println(name1 + "'s score: " + player1Score);
    
        // Start the game with player 2
        System.out.println(name2 + " LETS SEE WHAT YOU GOT! (ENTER QUIT TO END GAME)");
    
        // Get the score for player 2
        int player2Score = play(name2, "quit");
        System.out.println(name2 + "'s score: " + player2Score);
    
        // Compare the scores to determine the winner
        if (player1Score > player2Score) {
            System.out.println(name1 + " is the winner!");
        } else if (player2Score > player1Score) {
            System.out.println(name2 + " is the winner!");
        } else {
            System.out.println("It's a tie!");
        }
    }
}
