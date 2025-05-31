using UnityEngine;
using System.IO;

public class PlaneManager : MonoBehaviour
{
    public Texture2D texture; 
    public int brushSize = 5; 

    void Start()
    {

        Renderer renderer = GetComponent<Renderer>();
        if (renderer != null)
        {
            texture = new Texture2D(1024, 1024); 
            texture.wrapMode = TextureWrapMode.Clamp;
            renderer.material.mainTexture = texture; 
        }
        else
        {
            Debug.LogError("Plane nema Renderer komponentu!");
        }
    }

    void Update()
    {
    }

    public void PaintOnTexture(int x, int y, Color color)
    {
        for (int i = -brushSize; i <= brushSize; i++)
        {
            for (int j = -brushSize; j <= brushSize; j++)
            {
                int px = Mathf.Clamp(x + i, 0, texture.width - 1);
                int py = Mathf.Clamp(y + j, 0, texture.height - 1);

                texture.SetPixel(px, py, color);
            }
        }
        texture.Apply();
    }

    private void OnApplicationQuit()
    {
        SaveAsPNG();
    }

    public void SaveAsPNG()
    {
        if (texture == null)
        {
            Debug.LogError("Nema teksture za spremanje!");
            return;
        }

        if (!texture.isReadable)
        {
            Debug.LogError("Tekstura nije čitljiva! Provjeri Texture Import Settings.");
            return;
        }


        texture.Apply();


        Texture2D readableTexture = new Texture2D(texture.width, texture.height, TextureFormat.RGB24, false);

        readableTexture.SetPixels(texture.GetPixels());
        readableTexture.Apply();

        byte[] bytes = readableTexture.EncodeToPNG();

        string path = Application.dataPath + "/SavedTexture.png";
        File.WriteAllBytes(path, bytes);

        Debug.Log("Tekstura automatski spremljena u: " + path);
    }
}
