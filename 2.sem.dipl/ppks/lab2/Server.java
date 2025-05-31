import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.net.InetSocketAddress;

public class Server {
    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/", new MyHandler());
        server.start();
        System.out.println("Server started on port 8080");
    }

    static class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            String path = t.getRequestURI().getPath();
            if (path.equals("/")) {
                path = "index.html";
            }
            
            byte[] response;
            try {
                response = Files.readAllBytes(Paths.get(path));
                t.sendResponseHeaders(200, response.length);
            } catch (IOException e) {
                response = "404 Not Found".getBytes();
                t.sendResponseHeaders(404, response.length);
            }

            OutputStream os = t.getResponseBody();
            os.write(response);
            os.close();
        }
    }
}