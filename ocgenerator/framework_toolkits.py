# Copyright 2008-2015 Thomas Paviot (tpaviot@gmail.com)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# OpenCASCADE Toolkits: each ToolKit is a list of modules
#


FRAMEWORK_TOOLKITS = {
    'Foundation': {
        'TKernel': ['FSD', 'MMgt', 'OSD', 'Plugin', 'Quantity', 'Resource',
                    'SortTools',
                    'Standard', 'StdFail', 'Storage', 'TColStd',
                    'TCollection', 'TShort', 'Units', 'UnitsAPI',
                    'IncludeLibrary', 'Dico', 'NCollection', 'Message'],
        'TKMath': ['math', 'ElCLib', 'ElSLib', 'BSplCLib', 'BSplSLib',
                   'PLib', 'Precision', 'GeomAbs', 'Poly', 'CSLib',
                   'Convert', 'Bnd', 'gp', 'TColgp', 'TopLoc'],
        'TKAdvTools': ['Dynamic', 'Materials', 'Expr', 'ExprIntrp',
                       'GraphDS', 'GraphTools']},
    'Modeling': {
        'TKG2d': ['Geom2d', 'LProp', 'TColGeom2d', 'Adaptor2d',
                  'Geom2dLProp', 'Geom2dAdaptor', 'GProp'],
        'TKG3d': ['Geom', 'TColGeom', 'GeomAdaptor', 'AdvApprox',
                  'GeomLProp', 'Adaptor3d', 'LProp3d', 'TopAbs'],
        'TKGeomBase': ['ProjLib', 'GeomProjLib', 'GCPnts', 'CPnts',
                       'Approx', 'AppParCurves', 'FEmTool', 'AppCont',
                       'Extrema', 'IntAna', 'IntAna2d', 'GeomConvert',
                       'AdvApp2Var', 'GeomLib', 'Geom2dConvert', 'Hermit',
                       'BndLib', 'AppDef', 'GeomTools', 'GC', 'GCE2d',
                       'gce'],
        'TKBRep': ['TopoDS', 'TopExp', 'TopTools', 'BRep', 'BRepLProp',
                   'BRepAdaptor', 'BRepTools'],
        'TKGeomAlgo': ['Hatch', 'GeomInt', 'IntStart', 'IntWalk',
                       'IntImp', 'IntCurveSurface', 'IntSurf', 'IntPatch',
                       'Geom2dInt', 'IntImpParGen', 'IntRes2d', 'IntCurve',
                       'TopTrans', 'Intf', 'ApproxInt', 'TopTrans', 'Intf',
                       'ApproxInt', 'GccAna', 'GccEnt', 'GccInt', 'GccIter',
                       'GccGeo', 'HatchGen', 'Geom2dHatch', 'Law', 'TopTrans',
                       'Intf', 'ApproxInt', 'GccAna', 'GccEnt', 'GccInt',
                       'GccIter', 'GccGeo', 'HatchGen', 'Geom2dHatch',
                       'Law', 'AppBlend', 'Plate', 'GeomPlate',
                       'LocalAnalysis', 'GeomAPI', 'GeomFill', 'Geom2dAPI',
                       'Geom2dGcc', 'FairCurve', 'NLPlate', 'IntPolyh',
                       'TopClass'],
        'TKTopAlgo': ['IntCurvesFace', 'MAT', 'MAT2d', 'Bisector',
                      'BRepMAT2d', 'BRepCheck', 'BRepBndLib', 'BRepExtrema',
                      'BRepClass', 'BRepClass3d', 'BRepLib', 'BRepGProp',
                      'BRepIntCurveSurface', 'BRepTopAdaptor',
                      'BRepBuilderAPI', 'BRepApprox'],
        'TKPrim': ['BRepPrim', 'Primitives', 'BRepSweep', 'Sweep',
                   'BRepPrimAPI'],
        'TKBO': ['IntTools', 'BRepAlgoAPI', 'BOPCol', 'BOPInt', 'BOPDS',
                 'BOPAlgo', 'BOPTools'],
        'TKHLR': ['HLRTopoBRep', 'HLRBRep', 'HLRAlgo', 'HLRAppli',
                  'Intrv', 'TopBas', 'TopCnx', 'Contap'],
        'TKMesh': ['BRepMesh', 'IntPoly'],
        'TKShHealing': ['ShapeBuild', 'ShapeExtend', 'ShapeConstruct',
                        'ShapeCustom', 'ShapeAnalysis', 'ShapeFix',
                        'ShapeUpgrade', 'ShapeAlgo', 'ShapeProcess',
                        'ShapeProcessAPI'],
        'TKXMesh': ['XBRepMesh'],
        'TKBool': ['TopOpeBRep', 'TopOpeBRepDS', 'TopOpeBRepBuild',
                   'TopOpeBRepTool', 'BRepAlgo', 'BRepFill', 'BRepProj'],
        'TKFillet': ['ChFiDS', 'ChFi2d', 'ChFi3d', 'ChFiKPart', 'Blend',
                     'BRepBlend', 'BlendFunc', 'BRepFilletAPI',
                     'FilletSurf'],
        'TKFeat': ['LocOpe', 'BRepFeat'],
        'TKOffset': ['BRepOffsetAPI', 'Draft', 'BRepOffset', 'BiTgte'],
    },


    'Visualisation': {
        'TKService': ['Aspect', 'SelectBasics', 'Image',
                      'InterfaceGraphic', 'TColQuantity'],
        'TKV3d': ['V3d', 'Graphic3d', 'Visual3d', 'Select3D',
                  'Prs3d', 'StdPrs', 'SelectMgr', 'PrsMgr',
                  'AIS', 'DsgPrs', 'StdSelect'],
        'TKMeshVS': ['MeshVS'],
    },

    'DataExchange': {
        'TKSTL': ['StlMesh', 'StlAPI', 'StlTransfer', 'RWStl'],
        'TKSTEP': ['StepAP214', 'RWStepAP214', 'StepAP203', 'RWStepAP203',
                   'STEPConstruct', 'STEPEdit', 'GeomToStep', 'StepToGeom',
                   'StepToTopoDS', 'TopoDSToStep', 'STEPControl',
                   'STEPSelections', 'StepAP209'],
        'TKSTEPBase': ['StepBasic', 'RWStepBasic', 'StepRepr',
                       'RWStepRepr', 'StepGeom', 'RWStepGeom',
                       'StepShape', 'RWStepShape'],
        'TKIGES': ['IGESControl'],
        'TKXSBase': ['Interface', 'IFSelect', 'XSControl'],
    },

    'OCAF': {
        'TKCAF': ['TDataXtd', 'TNaming', 'TPrsStd', 'AppStd'],
        'TKCDF': [],
        'PTKernel': [],
        'TKLCAF': ['TDF', 'TDataStd', 'TFunction', 'TDocStd', 'AppStdL'],
        'FWOSPlugin': [],
        'TKPShape': [],
        'TKBinL': [],
        'TKXmlL': [],
        'TKPLCAF': [],
        'TKTObj': [],
        'TKShapeSchema': [],
        'TKStdLSchema': [],
        'TKXCAF': ['XCAFApp', 'XCAFDoc', 'XCAFPrs'],
        'TKXDESTEP': ['STEPCAFControl'],
        'TKXDEIGES': ['IGESCAFControl'],
    },

    'SMESH': {
        'SMESH': ['SMDSAbs', 'SMDS', 'SMESH', 'SMESHDS', 'StdMeshers', 'NETGENPlugin']
    },

    'VTK': {
        'TKIVtk': ['IVtk', 'IVtkOCC', 'IVtkVTK', 'IVtkTools']
    }
}
