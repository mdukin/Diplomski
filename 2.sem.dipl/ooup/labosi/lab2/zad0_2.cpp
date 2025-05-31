#include <iostream>
#include <assert.h>
#include <stdlib.h>
#include <list>

class Point{
public:
    int x;
    int y;
};

class Shape{
public:
    virtual void draw() = 0;
    virtual void move(Point* p)=0;
};

class Circle : public Shape{
private:
    double radius;
    Point center;
public:
    virtual void draw(){
        std::cerr << "in drawCircle\n";
    }
    virtual void move(Point* p){
        center.x+=p->x;
        center.y+=p->y;
        std::cerr << "in moveCircle\n";
    }
};
class Square : public Shape{
private:
    double side;
    Point center;
public:
    virtual void draw(){
        std::cerr << "in drawSquare\n";
    }

    virtual void move(Point* p){
        center.x+=p->x;
        center.y+=p->y;
        std::cerr << "in moveSquare\n";
    }
};

class Rhomb : public Shape{
private:
    double side;
    Point center;
public:
    virtual void draw(){
        std::cerr << "in drawRhomb\n";
    }

    virtual void move(Point* p){
        center.x+=p->x;
        center.y+=p->y;
        std::cerr << "in moveRhomb\n";
    }
};

typedef std::list <Shape*> Drawing;

void drawShapes(Drawing shapes){
   Drawing :: iterator it = shapes.begin ();
    while ( it != shapes.end()){
        (*it)->draw(); 
        ++ it;
    }
}

void moveShapes(Drawing shapes, Point* p){
    Drawing :: iterator it = shapes.begin ();
    while ( it != shapes.end()){
        (*it)->move(p); 
        ++it;
    }
}



int main()
{
    Drawing shapes;
    shapes.push_back(new Circle);
    shapes.push_back(new Square);
    shapes.push_back(new Square);
    shapes.push_back(new Circle);
    shapes.push_back(new Rhomb);

    Point *pointToMove =new Point;
    pointToMove->x=1;
    pointToMove->y=1;

    drawShapes(shapes);
    moveShapes(shapes, pointToMove);
    return 0;
}