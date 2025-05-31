using System;
using System.Net.Sockets;
using AssemblyCSharp.Assets.Scripts;
using UnityEngine;

public abstract class NetworkManager : IDisposable
{
    protected struct Constants
    {
        public const Int32 PORT = 13000;
    }


    protected GameManager gameManager;
    protected TcpClient tcpClient;
    protected UdpClient udpClient;

    protected NetworkManager(GameManager manager)
    {
        gameManager = manager;
    }


    public abstract void StartNetworkManager();


    public void Dispose()
    {
        Debug.Log("DISPOSE");
        // provjeriti je li UDP klijent postoji
        // ako UDP klijent postoji zatvoriti ga

        if (udpClient != null)
            udpClient.Close();
        // provjeriti je li TCP klijent postoji
        // ako postoji potrebno je
        // definirati novi responseBuffer
        // dohvatiti networkStream iz samog tcpClienta
        // definirati novi ProtokolData objekt i u njemu postaviti poruku na tip EXIT
        // u protokol data postaviti MoveSpace na NULL_SPACE - nije riječ o potezu
        //ostaviti ovaj dio koda vezan za kopiranje bytova s odgovarajućim offsetom)
        if (tcpClient != null)
        {
            NetworkStream stream = tcpClient.GetStream();
            byte[] responseBuffer = new byte[256];

            ProtocolData respHeader = new() { };

            respHeader.messageCode = ProtocolData.MessageCode.EXIT;
            respHeader.space = ProtocolData.MoveSpace.NULL_SPACE;

            Buffer.BlockCopy(BitConverter.GetBytes((int)respHeader.messageCode), 0, responseBuffer, 0, 4);
            Buffer.BlockCopy(BitConverter.GetBytes((int)respHeader.space), 0, responseBuffer, 4, 4);

            // zapisati odgovor iz response buffera u networkStream

            stream.Write(responseBuffer, 0, 8);
        }
    }


    public void SendMove(int move)
    {
        Debug.Log("sendmove");
        // isključiti u gameManageru mogućnost igranja kroz disable boeard
        // definirati novi buffer
        // dohvatiti networkStream iz samog tcpClienta
        // definirati novi ProtokolData objekt i u njemu postaviti poruku na tip MOVE
        // u protokol data postaviti MoveSpace na odgovarajuću vrijednost samog poteza

        gameManager.DisableBoard();

        NetworkStream stream = tcpClient.GetStream();
        byte[] buffer =new byte[256]; ;

        ProtocolData reqHeader = new() { };

        reqHeader.messageCode = ProtocolData.MessageCode.MOVE;
        reqHeader.space = (ProtocolData.MoveSpace) move;

        //ostaviti ovaj dio koda vezan za kopiranje bytova s odgovarajućim offsetom)
        Buffer.BlockCopy(BitConverter.GetBytes((int)reqHeader.messageCode), 0, buffer, 0, 4);
        Buffer.BlockCopy(BitConverter.GetBytes((int)reqHeader.space), 0, buffer, 4, 4);

        // zapisati buffer u networkStream      
        stream.Write(buffer, 0, 8);


    }


    public void Restart()
    {
        Debug.Log("restart");
        // definirati novi buffer
        // dohvatiti networkStream iz samog tcpClienta
        // definirati novi ProtokolData objekt i u njemu postaviti poruku na tip RESTART
        // u protokol data postaviti MoveSpace na na NULL_SPACE - nije riječ o potezu

        byte[] buffer = new byte[256];
        NetworkStream stream = tcpClient.GetStream();

        ProtocolData reqHeader = new() { };

        reqHeader.messageCode = ProtocolData.MessageCode.RESTART;
        reqHeader.space = ProtocolData.MoveSpace.NULL_SPACE;

        Buffer.BlockCopy(BitConverter.GetBytes((int)reqHeader.messageCode), 0, buffer, 0, 4);
        Buffer.BlockCopy(BitConverter.GetBytes((int)reqHeader.space), 0, buffer, 4, 4);

        stream.Write(buffer, 0, 8);
        // zapisati buffer u networkStream     
    }
}