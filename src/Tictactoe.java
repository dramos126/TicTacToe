import java.util.Scanner;

class Tictactoe {

    void playGame() {
        printBoard();

        while (boardIsNotFull()) {
            updateBoard();
            if (checkWinner()) {
                break;
            }
            switchPlayer();
        }
    }

    private static String[] POSITION = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
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
        String update = playerInput(CURRENT_PLAYER);
        for (int i = 0; i < POSITION.length; i++) {
            if (update.equals(POSITION[i])) {
                POSITION[i] = CURRENT_PLAYER;
            }
        }
        printBoard();
    }

    private String playerInput(String player) {
        Scanner scanner = new Scanner(System.in);
        String userInput;

        print("Player " + player + " select a position");

        do {
            userInput = scanner.nextLine();
        } while (userInputIsInvalid(userInput) || positionIsNotAvailable(userInput));

        return userInput;
    }

    private boolean userInputIsInvalid(String playerInput) {
        if (!playerInput.matches("[1-9]") || playerInput.length() != 1) {
            print("Invalid input, please try again.");
            return true;
        }
        return false;
    }

    private boolean positionIsNotAvailable(String playerInput) {
        for (int i = 0; i < POSITION.length; i++) {
            if (playerInput.equals(POSITION[i]) && POSITION[i].matches("[1-9]")) {
                return false;
            }
        }
        print("Position " + playerInput + " is full, try again");
        return true;
    }

    private boolean checkWinner() {
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
            if (!position.matches("[1-9]")) {
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
        if (CURRENT_PLAYER.equals(PLAYERS[0])) {
            CURRENT_PLAYER = PLAYERS[1];
        } else {
            CURRENT_PLAYER = PLAYERS[0];
        }
    }

    private void print(String whatToPrint) {
        System.out.println(whatToPrint);
    }
}