using UnityEngine;

public class Spring : MonoBehaviour
{
    public Particle particleA; 
    public Transform topOfSpring; 
    public float restLength = 1f; // normalna duljina 
    public float k = 10f; // koeficijent
    public float prigusenje = 0.1f; // Prigušenje
    private LineRenderer lineRenderer; 

    void Start()
    {
        lineRenderer = GetComponent<LineRenderer>();
        if (lineRenderer == null)
        {
            lineRenderer = gameObject.AddComponent<LineRenderer>();
            lineRenderer.material = new Material(Shader.Find("Unlit/Color"));
            lineRenderer.startColor = Color.green;
            lineRenderer.endColor = Color.green;
            lineRenderer.startWidth = 0.05f;
            lineRenderer.endWidth = 0.05f;
            lineRenderer.positionCount = 2;
        }
    }

    void Update()
    {

        Vector3 delta = topOfSpring.position - particleA.transform.position;
        float currentLength = delta.magnitude;
        float dx = currentLength - restLength;

        Vector3 force = k * dx * delta.normalized - prigusenje * particleA.velocity;

        particleA.ApplyForce(force);

        if (lineRenderer != null)
        {
            lineRenderer.SetPosition(0, topOfSpring.position);
            lineRenderer.SetPosition(1, particleA.transform.position);
        }
    }
}
