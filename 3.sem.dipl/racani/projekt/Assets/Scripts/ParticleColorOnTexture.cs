using UnityEngine;

public class ParticleColorOnTexture : MonoBehaviour
{
    public PlaneManager planeManager; 
    public Color particleColor = Color.red;
    private ParticleSystem particleSystem;

    void Start() { 

        GameObject planeObject = GameObject.Find("Pod"); 
        if (planeObject != null)
        {
            planeManager = planeObject.GetComponent<PlaneManager>();
            if (planeManager == null)
            {
                Debug.LogError("Nema PlaneManager komponente na objektu!");
            }
        }
        else
        {
            Debug.LogError("Nema objekta 'Pod' u sceni!");
        }

        particleSystem = GetComponentInChildren<ParticleSystem>();
        if (particleSystem != null)
        {
            var mainModule = particleSystem.main;
            mainModule.startColor = particleColor;
        }
        else
        {
            Debug.LogError("Nema ParticleSystem komponente ispod ovog objekta!");
        }
    }

    void Update()
    {
        if (planeManager != null)
        {

            Vector3 particlePosition = transform.position;


            Vector2 uv = WorldPositionToUV(particlePosition); //x,z
            
            // (0->1)
            int x = Mathf.FloorToInt(uv.x * planeManager.texture.width);
            int y = Mathf.FloorToInt(uv.y * planeManager.texture.height);

            planeManager.PaintOnTexture(x, y, particleColor);
        }
    }

    Vector2 WorldPositionToUV(Vector3 worldPosition)
    {
        Vector3 planePosition = planeManager.transform.position;
        Vector3 planeSize = planeManager.GetComponent<Renderer>().bounds.size;

        float u = (worldPosition.x + (planeSize.x/2)) / planeSize.x; // Skaliraj u odnosu na širinu objekta
        float v = (worldPosition.z + (planeSize.z /2)) / planeSize.z; // Skaliraj u odnosu na visinu objekta

        u = 1 - u;
        v = 1 - v;
        return new Vector2(u, v);
    }

}
