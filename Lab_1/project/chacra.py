import vtk
import random
import house as h
import arbol as abl


# source
## Arbol
### Tronco y Hojas
tree = abl.Tree()

## Casa
house = h.House()

# mapper
## Arbol
### Tronco
mapperTrunk = tree.SetTrunk(0.3,2.6,50)#radio,height,resolution

### Hojas
mapperLeaf = tree.SetLeaf(0.3,500)#radio,resolution

## Casa
mapperChapa = house.SetSphere(0.1)#radio
mapperCone = house.SetCone(1.9,1.6,50)#radio,height,resolution
mapperCube1 = house.SetCube(2.5,2.5,2.5)#cuerpo
mapperCube2 = house.SetCube(1.2,1.8,0.2)#puerta
mapperCube3 = house.SetCube(0.1,1.1,1.4)#ventana

## Cerros
mapperCerro1 = house.SetCone(10.0,15.0,60)#radio,height,resolution

## Cerros
actorCerro1 = house.SetActorCube(mapperCerro1,11/255, 83/255, 69/255 ,7.0,5.0,-30.0)#color and pos
actorCerro2 = house.SetActorCube(mapperCerro1,11/255, 83/255, 69/255 ,-7.0,5.0,-30.0)#color and pos

## Casa
### Cube
actorCube1 = house.SetActorCube(mapperCube1,235/255, 161/255, 52/255,0,0,0)#color and pos
actorCube2 = house.SetActorCube(mapperCube2,235/255, 116/255, 52/255,0.0,-0.3,1.5)#color and pos
actorCube3 = house.SetActorCube(mapperCube3,130/255, 185/255, 189/255,-1.5,0,0)#color and pos

### Cone
actorCone = house.SetActorCube(mapperCone,142/255, 156/255, 151/255,0,2.0,0)#color and pos

### Chapa
actorChapa = house.SetActorCube(mapperChapa,99/255, 87/255, 22/255,-0.4,-0.3,1.6)#color and pos

#actor
## Arbol
### Tronco
actorTrunk = tree.SetActorTrunk(mapperTrunk,2,0.0,1.5)#mapperTrunk,posx,posy,posz
actorTrunk2 = tree.SetActorTrunk(mapperTrunk,-2,0.0,1.5)#mapperTrunk,posx,posy,posz

###Hojas
#establecer las esferas
arraySphere = tree.SetTree(50,2,1.6,1.5)#cantidad,posx,posy,posz raiz
arraySphere2 = tree.SetTree(25,-2,1.6,1.5)#cantidad,posx,posy,posz raiz

#axes
transform = vtk.vtkTransform()
transform.Translate(1.5, 0.0, 0.0) 
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transform)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actorTrunk)
renderer.AddActor(actorTrunk2)
for pointLeaf in arraySphere:
    actorLeaf_aux = tree.SetActorLeaf(mapperLeaf,pointLeaf.x,pointLeaf.y,pointLeaf.z)
    renderer.AddActor(actorLeaf_aux)
for pointLeaf in arraySphere2:
    actorLeaf_aux = tree.SetActorLeaf(mapperLeaf,pointLeaf.x,pointLeaf.y,pointLeaf.z)
    renderer.AddActor(actorLeaf_aux)
#renderer.AddActor(axes)
## Casa
renderer.AddActor(actorCube1)
renderer.AddActor(actorCube2)
renderer.AddActor(actorCube3)
renderer.AddActor(actorCone)
renderer.AddActor(actorChapa)
renderer.AddActor(actorCerro1)
renderer.AddActor(actorCerro2)


###### Estableciendo mas arboles
quantityTree = 100
for i in range(quantityTree):
    positionX=random.uniform(-30,30)
    positionZ=random.uniform(-30,30)
    while(positionX >= -2.5 and positionX <=2.5):
        positionX=random.uniform(-30,30)
    while(positionZ >= -2.5 and positionZ <=2.5):
        positionZ=random.uniform(-30,30)

    actorTrunk_aux = tree.SetActorTrunk(mapperTrunk,positionX,0.0,positionZ)
    quantityLeaf=random.randint(5,50)
    arraySphere_aux = tree.SetTree(quantityLeaf,positionX,1.6,positionZ)
    renderer.AddActor(actorTrunk_aux)
    for pointLeaf in arraySphere_aux:
        actorLeaf_aux = tree.SetActorLeaf(mapperLeaf,pointLeaf.x,pointLeaf.y,pointLeaf.z)
        renderer.AddActor(actorLeaf_aux)



 


#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
