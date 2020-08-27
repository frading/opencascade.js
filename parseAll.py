#!/usr/bin/python3.8

import subprocess
import os

occtFiles = [
  # BRepBuilderAPI
  "BRepBuilderAPI_BndBoxTreeSelector.hxx",
  "BRepBuilderAPI_CellFilter.hxx",
  "BRepBuilderAPI_Collect.hxx",
  "BRepBuilderAPI_Command.hxx",
  "BRepBuilderAPI_Copy.hxx",
  "BRepBuilderAPI_EdgeError.hxx",
  "BRepBuilderAPI_FaceError.hxx",
  "BRepBuilderAPI_FastSewing.hxx",
  "BRepBuilderAPI_FindPlane.hxx",
  "BRepBuilderAPI_GTransform.hxx",
  "BRepBuilderAPI.hxx",
  "BRepBuilderAPI_MakeEdge2d.hxx",
  "BRepBuilderAPI_MakeEdge.hxx",
  "BRepBuilderAPI_MakeFace.hxx",
  "BRepBuilderAPI_MakePolygon.hxx",
  "BRepBuilderAPI_MakeShape.hxx",
  "BRepBuilderAPI_MakeShell.hxx",
  "BRepBuilderAPI_MakeSolid.hxx",
  "BRepBuilderAPI_MakeVertex.hxx",
  "BRepBuilderAPI_MakeWire.hxx",
  "BRepBuilderAPI_ModifyShape.hxx",
  "BRepBuilderAPI_NurbsConvert.hxx",
  "BRepBuilderAPI_PipeError.hxx",
  "BRepBuilderAPI_Sewing.hxx",
  "BRepBuilderAPI_ShapeModification.hxx",
  "BRepBuilderAPI_ShellError.hxx",
  "BRepBuilderAPI_Transform.hxx",
  "BRepBuilderAPI_TransitionMode.hxx",
  "BRepBuilderAPI_VertexInspector.hxx",
  "BRepBuilderAPI_WireError.hxx",

  # GC
  "GC_MakeArcOfCircle.hxx",
  "GC_MakeArcOfEllipse.hxx",
  "GC_MakeArcOfHyperbola.hxx",
  "GC_MakeArcOfParabola.hxx",
  "GC_MakeCircle.hxx",
  "GC_MakeConicalSurface.hxx",
  "GC_MakeCylindricalSurface.hxx",
  "GC_MakeEllipse.hxx",
  "GC_MakeHyperbola.hxx",
  "GC_MakeLine.hxx",
  "GC_MakeMirror.hxx",
  "GC_MakePlane.hxx",
  "GC_MakeRotation.hxx",
  "GC_MakeScale.hxx",
  "GC_MakeSegment.hxx",
  "GC_MakeTranslation.hxx",
  "GC_MakeTrimmedCone.hxx",
  "GC_MakeTrimmedCylinder.hxx",
  "GC_Root.hxx",

  # gp
  "gp_Ax1.hxx",
  "gp_Ax22d.hxx",
  "gp_Ax2d.hxx",
  "gp_Ax2.hxx",
  "gp_Ax3.hxx",
  "gp_Circ2d.hxx",
  "gp_Circ.hxx",
  "gp_Cone.hxx",
  "gp_Cylinder.hxx",
  "gp_Dir2d.hxx",
  "gp_Dir.hxx",
  "gp_Elips2d.hxx",
  "gp_Elips.hxx",
  "gp_EulerSequence.hxx",
  "gp_GTrsf2d.hxx",
  "gp_GTrsf.hxx",
  "gp.hxx",
  "gp_Hypr2d.hxx",
  "gp_Hypr.hxx",
  "gp_Lin2d.hxx",
  "gp_Lin.hxx",
  "gp_Mat2d.hxx",
  "gp_Mat.hxx",
  "gp_Parab2d.hxx",
  "gp_Parab.hxx",
  "gp_Pln.hxx",
  "gp_Pnt2d.hxx",
  "gp_Pnt.hxx",
  "gp_Quaternion.hxx",
  "gp_QuaternionNLerp.hxx",
  "gp_QuaternionSLerp.hxx",
  "gp_Sphere.hxx",
  "gp_Torus.hxx",
  "gp_Trsf2d.hxx",
  "gp_TrsfForm.hxx",
  "gp_Trsf.hxx",
  "gp_TrsfNLerp.hxx",
  "gp_Vec2d.hxx",
  "gp_Vec.hxx",
  "gp_VectorWithNullMagnitude.hxx",
  "gp_XY.hxx",
  "gp_XYZ.hxx",

  # TopoDS
  "TopoDS_AlertWithShape.hxx",
  "TopoDS_Builder.hxx",
  "TopoDS_Compound.hxx",
  "TopoDS_CompSolid.hxx",
  "TopoDS_Edge.hxx",
  "TopoDS_Face.hxx",
  "TopoDS_FrozenShape.hxx",
  "TopoDS_HShape.hxx",
  "TopoDS.hxx",
  "TopoDS_Iterator.hxx",
  "TopoDS_ListIteratorOfListOfShape.hxx",
  "TopoDS_ListOfShape.hxx",
  "TopoDS_LockedShape.hxx",
  "TopoDS_Shape.hxx",
  "TopoDS_Shell.hxx",
  "TopoDS_Solid.hxx",
  "TopoDS_TCompound.hxx",
  "TopoDS_TCompSolid.hxx",
  "TopoDS_TEdge.hxx",
  "TopoDS_TFace.hxx",
  "TopoDS_TShape.hxx",
  "TopoDS_TShell.hxx",
  "TopoDS_TSolid.hxx",
  "TopoDS_TVertex.hxx",
  "TopoDS_TWire.hxx",
  "TopoDS_UnCompatibleShapes.hxx",
  "TopoDS_Vertex.hxx",
  "TopoDS_Wire.hxx"
]

for occtFile in occtFiles:
  moduleName = occtFile.split('_')[0]
  if moduleName == occtFile:
    moduleName = os.path.splitext(occtFile)[0]
  inputFile = "./build/occt/src/" + moduleName + "/" + occtFile
  if not os.path.exists("./embind/" + moduleName):
    os.makedirs("./embind/" + moduleName)
  outputFile = "./embind/" + moduleName + "/" + os.path.splitext(occtFile)[0] + ".h"
  subprocess.call(['./parse.py', inputFile, outputFile])
