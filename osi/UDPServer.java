import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class UDPServer {
    public static void main(String[] args) {
        int port = 5000;

        try (DatagramSocket serverSocket = new DatagramSocket(port)) {
            System.out.println("UDP Server siap menerima pesan di port " + port + "...");
            byte[] receiveBuffer = new byte[1024];

            while (true) {
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                serverSocket.receive(receivePacket);

                String message = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("[" + receivePacket.getAddress().getHostAddress() + ":"
                        + receivePacket.getPort() + "] Pesan: " + message);

                // Ubah jadi huruf kapital lalu balas ke client asal
                byte[] replyBuffer = message.toUpperCase().getBytes();
                DatagramPacket replyPacket = new DatagramPacket(
                        replyBuffer, replyBuffer.length,
                        receivePacket.getAddress(), receivePacket.getPort());
                serverSocket.send(replyPacket);
            }
        } catch (Exception e) {
            System.err.println("Terjadi kesalahan pada Server: " + e.getMessage());
        }
    }
}