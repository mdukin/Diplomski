using Unity.Netcode;
using UnityEngine;
using Unity.Collections;
using System;

public class PlayerManager : NetworkBehaviour
{
    public float moveSpeed = 5f;
    private NetworkManager networkManager;
    private GameManager gameManager;
    private Vector3 spawnPoint1 = new Vector3(11f, 1.5f, 0f);
    private Vector3 spawnPoint2 = new Vector3(0f, 1.5f, 11f);
    private bool canMove = false;
    private MeshRenderer playerMeshRenderer;
    //TODO: this network variable needs to be readable by everyone and can be written only by owner
    private NetworkVariable<FixedString512Bytes> playerName = new NetworkVariable<FixedString512Bytes>(
        writePerm: NetworkVariableWritePermission.Owner,
        readPerm: NetworkVariableReadPermission.Everyone);

    private void Update()
    {
        if (IsOwner && canMove)
        {
            Movement();
        }
    }

    // TODO
    public override void OnNetworkSpawn()
    {
        base.OnNetworkSpawn();
        networkManager = FindObjectOfType<NetworkManager>();
        gameManager = FindObjectOfType<GameManager>();


        if (!IsOwner) return;

        if (networkManager.IsHost)
        {
            Debug.Log("Postavljanje hosta na spawnPoint1");
            transform.SetPositionAndRotation(spawnPoint1, Quaternion.identity);
            playerName.Value = "Host";
        }

        else if (networkManager.IsClient)
        {
            Debug.Log("Postavljanje klijenta na spawnPoint2");
            transform.SetPositionAndRotation(spawnPoint2, Quaternion.identity);
            playerName.Value = "Client";
        }

    }

    private void Start()
    {
        playerMeshRenderer = this.GetComponent<MeshRenderer>();
    }
     
    void Movement()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        Vector3 moveDirection = new Vector3(horizontalInput, 0f, verticalInput).normalized;

        MovePlayer(moveDirection);
    }

    void MovePlayer(Vector3 moveDirection)
    {
        transform.Translate(moveDirection * moveSpeed * Time.deltaTime);
    }

    public void ResetPosition()
    {
        if (IsOwner && networkManager.IsHost)
        {
            transform.SetPositionAndRotation(spawnPoint1, new Quaternion());
        }
        else if (IsOwner && networkManager.IsClient)
        {
            transform.SetPositionAndRotation(spawnPoint2, new Quaternion());
        }
    }

    public void EnableMovement()
    {
        canMove = true;
    }

    public void DisableMovement()
    {
        canMove = false;
    }

    public string GetPlayerName()
    {
        return playerName.Value.ToString();
    }

    public void SetColor(Color color)
    {
        ChangeColorRpc(color);
    }

    // TODO: All entities should activate this function
    [Rpc(SendTo.Everyone)]
    private void ChangeColorRpc(Color color)
    {
            if (playerMeshRenderer != null)
            {
                playerMeshRenderer.material.color = color;
            }

            var playerChildManager = GetComponentInChildren<PlayerChildManager>();
            if (playerChildManager != null)
            {
                playerChildManager.SetColor(color);
                Debug.Log(color);
            }
            else
            {
                Debug.LogWarning("playerChildManager not found");
            }

            gameManager.PlayerReady();
        

    }


}
