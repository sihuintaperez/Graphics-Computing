import vtk
import math
import random
#Class for the Sphere
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Tree:

    def SetTrunk(self,radio,height,resolution):      
        self.cylinder = vtk.vtkCylinderSource()
        self.cylinder.SetRadius(radio)
        self.cylinder.SetHeight(height)
        self.cylinder.SetResolution(resolution)
        self.cylinder.Update()
        #mapper
        mapper= vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.cylinder.GetOutput())
        return mapper
        
    def SetLeaf(self,radio,resolution):
        
        self.sphere = vtk.vtkSphereSource()
        self.sphere.SetRadius(radio)
        # ##Make the surface smooth.
        self.sphere.SetPhiResolution(resolution)
        self.sphere.SetThetaResolution(resolution)
        self.sphere.Update()
        #mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.sphere.GetOutput())
        return mapper
    def SetActorTrunk(self,mapperTrunk,posX,posY,posZ):
        actor = vtk.vtkActor()
        actor.SetMapper(mapperTrunk)
        actor.GetProperty().SetColor(86/255, 47/255, 47/255)
        #actorTrunk.RotateX(20.0)
        actor.SetPosition(posX,posY,posZ)
        return actor

    def SetActorLeaf(self,mapperLeaf,posX,posY,posZ):
        actor = vtk.vtkActor()
        actor.SetMapper(mapperLeaf)
        actor.GetProperty().SetColor(0.0, 1.0, 0.0)
        actor.SetPosition(posX,posY,posZ)
        return actor

    def SetTree(self,quantitySphere,ejeXPoint,ejeYPoint,ejeZPoint):#quantitySphere>=5

        topbyNivel = int(math.log(quantitySphere,4)) #altura del arbol 4^n
        dia = 0.4 
        point = Point(ejeXPoint,ejeYPoint+(dia * topbyNivel),ejeZPoint) #maxima altura RAIZ

        arraySphere = []
        quantitySphere -=1

        indexArray = 0
        for quantityNivel in range(1,topbyNivel+2): #uno mas para los restantes
            qSphereSave = 4**quantityNivel
            if (quantitySphere >= qSphereSave):
                quantitySphere -= qSphereSave
                if (len(arraySphere) == 0):
                    pointXPos = Point(ejeXPoint+0.3,(ejeYPoint+(dia * topbyNivel)-dia),ejeZPoint)
                    pointXNeg = Point(ejeXPoint-0.3,(ejeYPoint+(dia * topbyNivel)-dia),ejeZPoint) 
                    pointZPos = Point(ejeXPoint,(1.6+(dia * topbyNivel)-dia),ejeZPoint+0.3) 
                    pointZNeg = Point(ejeXPoint,(1.6+(dia * topbyNivel)-dia),ejeZPoint-0.3) 
                    arraySphere.append(pointXPos)
                    arraySphere.append(pointXNeg)
                    arraySphere.append(pointZPos)
                    arraySphere.append(pointZNeg)
                
                else:
                    for i in range(indexArray,len(arraySphere)):
                        pointXPos = Point(arraySphere[i].x+0.3,arraySphere[i].y-dia,arraySphere[i].z)
                        pointXNeg = Point(arraySphere[i].x-0.3,arraySphere[i].y-dia,arraySphere[i].z)
                        pointZPos = Point(arraySphere[i].x,arraySphere[i].y-dia,arraySphere[i].z+0.3)
                        pointZNeg = Point(arraySphere[i].x,arraySphere[i].y-dia,arraySphere[i].z-0.3)
                        arraySphere.append(pointXPos)
                        arraySphere.append(pointXNeg)
                        arraySphere.append(pointZPos)
                        arraySphere.append(pointZNeg)
                    indexArray = 4**(quantityNivel-1)
                
            else:
                
                if(len(arraySphere) == 0):
                    print('hola')
                else:
                    for i in range(quantitySphere):
                        leafRandom=random.randint(indexArray, len(arraySphere)-1)
                        position=random.randint(1, 4)
                        if (position == 1):
                            pointXPos = Point(arraySphere[leafRandom].x+0.1,arraySphere[leafRandom].y-dia+0.2,arraySphere[leafRandom].z)
                            arraySphere.append(pointXPos)
                        elif (position == 2):
                            pointXNeg = Point(arraySphere[leafRandom].x-0.1,arraySphere[leafRandom].y-dia+0.2,arraySphere[leafRandom].z)
                            arraySphere.append(pointXNeg)
                        elif (position == 3):
                            pointZPos = Point(arraySphere[leafRandom].x,arraySphere[leafRandom].y-dia+0.2,arraySphere[leafRandom].z+0.1)
                            arraySphere.append(pointZPos)
                        elif (position == 4):
                            pointZNeg = Point(arraySphere[leafRandom].x,arraySphere[leafRandom].y-dia+0.2,arraySphere[leafRandom].z-0.1)
                            arraySphere.append(pointZNeg)
        arraySphere.append(point)
        return arraySphere
