using UnityEngine;
using Unity.Netcode;

public class MenuManager : MonoBehaviour
{
    private NetworkManager networkManager;

    private void Start()
    {
        networkManager = FindObjectOfType<NetworkManager>();
    }

    // TODO
    public void StartHost()
    {
        //Start host through networkManager
        if (networkManager != null)
        {
            networkManager.StartHost();
            Debug.Log("Host je pokrenut.");
        }
        else
        {
            Debug.LogError("NetworkManager nije pronađen!");
        }
    }

    // TODO
    public void StartClient()
    {
        //Start client through networkManager
        if (networkManager != null)
        {
            networkManager.StartClient();
            Debug.Log("Klijent je pokrenut.");
        }
        else
        {
            Debug.LogError("NetworkManager nije pronađen!");
        }
    }

    public void QuitGame()
    {
        Application.Quit();
    }
}
