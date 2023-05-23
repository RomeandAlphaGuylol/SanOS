import javax.swing.*;
public class Game {
    public static void main(String[] args){
        JFrame frame = new JFrame();
        JButton button = new JButton("Kill");
        

        button.setBounds(128, 19, 150, 90);
        frame.add(button);
        frame.setLayout(null);
        frame.setVisible(true);
    }
}