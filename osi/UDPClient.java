import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class UDPClient {
    public static void main(String[] args) {
        String serverHost = "localhost";
        int serverPort = 5000;

        try (DatagramSocket clientSocket = new DatagramSocket();
             Scanner scanner = new Scanner(System.in)) {

            InetAddress serverAddress = InetAddress.getByName(serverHost);
            System.out.println("Ketik pesan (ketik EXIT untuk keluar):");

            while (true) {
                System.out.print("> ");
                String messageStr = scanner.nextLine();

                if (messageStr.equalsIgnoreCase("EXIT")) {
                    System.out.println("Client keluar.");
                    break;
                }

                byte[] sendBuffer = messageStr.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(
                        sendBuffer, sendBuffer.length, serverAddress, serverPort);
                clientSocket.send(sendPacket);

                byte[] receiveBuffer = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                clientSocket.receive(receivePacket);

                String reply = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("[Server]: " + reply);
            }
        } catch (Exception e) {
            System.err.println("Terjadi kesalahan pada Client: " + e.getMessage());
        }
    }
}