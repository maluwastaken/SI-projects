# The "Food" class

class Food():

    def __init__(self, pos, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = pos
        self.r = 5
        self.maxspeed = 1.0
        self.maxforce = 0.01
        
    def reset(self, pos, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = pos
        
    def getPosition(self):
        return self.position
    
    def star(self):
        radius1 = self.r * 1.3
        radius2 = self.r * 0.6
        npoints = 4
        angle = TWO_PI / npoints
        a = 0
        halfAngle = angle/2.0
        x = 0
        y = 0
        beginShape()
        while (a < TWO_PI):
            sx = x + cos(a) * radius2
            sy = y + sin(a) * radius2
            vertex(sx, sy)
            sx = x + cos(a+halfAngle) * radius1
            sy = y + sin(a+halfAngle) * radius1
            vertex(sx, sy)
            a += angle
        endShape(CLOSE)
        
    # Method to update location
    def update(self, position):
        self.position = position
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading()# + PI / 2
        #fill(12)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            self.star()
            
    
        
        
        
