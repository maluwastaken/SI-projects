# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class
class Vehicle():

    def __init__(self, pos, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = pos
        self.r = 4
        self.maxspeed = 5
        self.maxforce = 10
        
    def getPosition(self):
        return self.position
        
    def reset(self, pos, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = pos

    def checkTerrain(self, mat, tl):
        position = self.position/tl
        #
        #print(str(int(position.x)) + ' ' +  str(int(position.y)))
        #print(mat[int(position.x)][int(position.y)])
        #print(mat[int(position.x)])
        self.maxspeed = mat[int(floor(self.position.x/tl))][int(floor(self.position.y/tl))]

        if int(floor(self.position.x/tl)) > 63 or int(floor(self.position.x/tl)) < 0 or int(floor(self.position.y/tl)) < 0 or int(floor(self.position.y/tl)) > 35:
            self.maxspeed = 0
        

    # Method to update location
    def update(self, mat, tl):
        # Update velocity
        self.checkTerrain(mat, tl)
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
        theta = self.velocity.heading() + PI / 2
        fill(127)
        stroke(125, 0, 0)
        strokeWeight(1)
        print(theta)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
        
    def chase(self, food):
        pos = food - self.position #get position vector
        dir = pos - self.velocity #get direction to apply force to
        self.applyForce(dir)
    
    
