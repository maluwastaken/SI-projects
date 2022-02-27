# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class
class Vehicle():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 5
        self.maxforce = 1

    def checkTerrain(self, mat, tl):
        position = self.position/tl
        #
        #print(str(int(position.x)) + ' ' +  str(int(position.y)))
        #print(mat[int(position.x)][int(position.y)])
        #print(mat[int(position.x)])
        self.maxspeed = mat[int(position.x)][int(position.y)]
        #print(self.velocity)
        

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
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
            
    def arrive(self, target):

        # A vector pointing from the location to the target
        desired = target - self.position
        d = desired.mag()

        # Scale with arbitrary damping within 100 pixels
        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)
        
    def chase(self, food):
        pos = food - self.position #get position vector
        dir = pos - self.velocity #get direction to apply force to
        self.applyForce(dir)
    
