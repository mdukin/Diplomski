using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.Netcode;

public class HoleManager : NetworkBehaviour
{
    private MeshRenderer floorRenderer;

    private void Start()
    {
        floorRenderer = GetComponent<MeshRenderer>();
        floorRenderer.material.color = Color.black;
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") )
        {
            var playerNetworkObject = other.GetComponent<NetworkObject>();
            if (playerNetworkObject != null)
            {
                ResetPlayerPositionRpc(playerNetworkObject.NetworkObjectId);
            }
        }
    }

    [Rpc(SendTo.Everyone)]
    private void ResetPlayerPositionRpc(ulong playerNetworkObjectId)
    {
        NetworkObject playerNetworkObject = NetworkManager.SpawnManager.SpawnedObjects[playerNetworkObjectId];

        if (playerNetworkObject != null)
        {
            var playerManager = playerNetworkObject.GetComponent<PlayerManager>();
            if (playerManager != null)
            {
                playerManager.ResetPosition();
            }
        }
    }
}
