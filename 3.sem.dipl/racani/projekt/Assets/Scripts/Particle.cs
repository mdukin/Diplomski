using UnityEngine;

public class Particle : MonoBehaviour
{
    public Vector3 velocity; 
    public float mass = 1f; 
    public Vector3 gravity = new Vector3(0, -9.81f, 0); 
    private Vector3 acceleration;


    public void ApplyForce(Vector3 force)
    {
        acceleration += force / mass;
    }

    void Update()
    {
        ApplyForce(gravity * mass); // F = m * g

        velocity += acceleration * Time.deltaTime; 
        transform.position += velocity * Time.deltaTime;

        acceleration = Vector3.zero;
    }
}
