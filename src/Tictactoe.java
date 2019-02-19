import java.util.Scanner;

class Tictactoe {

    void playGame() {
        printBoard();

        while (boardIsNotFull()) {
            updateBoard();
            if (playerHasWon()) {
                break;
            }
            switchPlayer();
        }
    }

    private static final String[] POSITION = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
    private static final String DIGITS = "[1-9]";
    private static String[] PLAYERS = {"X", "O"};
    private static String CURRENT_PLAYER = PLAYERS[0];


    private void printBoard() {
        print(POSITION[0] + "|" + POSITION[1] + "|" + POSITION[2]);
        print("-+-+-");
        print(POSITION[3] + "|" + POSITION[4] + "|" + POSITION[5]);
        print("-+-+-");
        print(POSITION[6] + "|" + POSITION[7] + "|" + POSITION[8]);
    }


    private void updateBoard() {
        String update = playerInput();
        for (int i = 0; i < POSITION.length; i++) {
            if (update.equals(POSITION[i])) {
                POSITION[i] = CURRENT_PLAYER;
            }
        }
        printBoard();
    }

    private String playerInput() {
        Scanner scanner = new Scanner(System.in);
        String userInput;

        print("Player " + CURRENT_PLAYER + " turn, please select");

        do {
            userInput = scanner.nextLine();
        } while (userInputIsInvalid(userInput) || positionIsNotAvailable(userInput));

        return userInput;
    }

    private boolean userInputIsInvalid(String playerInput) {
        if (!playerInput.matches(DIGITS) || playerInput.length() != 1) {
            print("Invalid position, please try again.");
            return true;
        }
        return false;
    }

    private boolean positionIsNotAvailable(String playerInput) {
        for (String aPOSITION : POSITION) {
            if (playerInput.equals(aPOSITION) && aPOSITION.matches(DIGITS)) {
                return false;
            }
        }
        print("Position " + playerInput + " is full, try again");
        return true;
    }

    private boolean playerHasWon() {
        boolean win[] = {
                POSITION[0].matches(CURRENT_PLAYER) && POSITION[1].matches(CURRENT_PLAYER) && POSITION[2].matches(CURRENT_PLAYER),
                POSITION[3].matches(CURRENT_PLAYER) && POSITION[4].matches(CURRENT_PLAYER) && POSITION[5].matches(CURRENT_PLAYER),
                POSITION[6].matches(CURRENT_PLAYER) && POSITION[7].matches(CURRENT_PLAYER) && POSITION[8].matches(CURRENT_PLAYER),
                POSITION[0].matches(CURRENT_PLAYER) && POSITION[3].matches(CURRENT_PLAYER) && POSITION[6].matches(CURRENT_PLAYER),
                POSITION[1].matches(CURRENT_PLAYER) && POSITION[4].matches(CURRENT_PLAYER) && POSITION[7].matches(CURRENT_PLAYER),
                POSITION[2].matches(CURRENT_PLAYER) && POSITION[5].matches(CURRENT_PLAYER) && POSITION[8].matches(CURRENT_PLAYER),
                POSITION[0].matches(CURRENT_PLAYER) && POSITION[4].matches(CURRENT_PLAYER) && POSITION[8].matches(CURRENT_PLAYER),
                POSITION[2].matches(CURRENT_PLAYER) && POSITION[4].matches(CURRENT_PLAYER) && POSITION[6].matches(CURRENT_PLAYER),
        };

        if (win[0] || win[1] || win[2] || win[3] || win[4] || win[5] || win[6] || win[7]) {
            print("Player " + CURRENT_PLAYER + " Has WON!");
            return true;
        }
        return false;
    }

    private boolean boardIsNotFull() {
        int openSpots = POSITION.length;

        for (String position : POSITION) {
            if (!position.matches(DIGITS)) {
                openSpots--;
            }
        }

        if (openSpots == 0) {
            print("Game Over");
            return false;
        }
        return true;
    }

    private void switchPlayer() {
        CURRENT_PLAYER = (CURRENT_PLAYER.equals(PLAYERS[0])) ? PLAYERS[1] : PLAYERS[0];
    }

    private void print(String whatToPrint) {
        System.out.println(whatToPrint);
    }
}