# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Solution', [dirname(__file__)])
        except ImportError:
            import _Solution
            return _Solution
        if fp is not None:
            try:
                _mod = imp.load_module('_Solution', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Solution = swig_import_helper()
    del swig_import_helper
else:
    import _Solution
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Solution(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solution, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Solution, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["solution"] = lambda x: _Solution.Solution_solution
    if _newclass:solution = staticmethod(_Solution.Solution_solution)
    def solve(self): return _Solution.Solution_solve(self)
    def addSolution(self, *args): return _Solution.Solution_addSolution(self, *args)
    def clear(self): return _Solution.Solution_clear(self)
    def cubatureEnrichmentDegree(self): return _Solution.Solution_cubatureEnrichmentDegree(self)
    def setCubatureEnrichmentDegree(self, *args): return _Solution.Solution_setCubatureEnrichmentDegree(self, *args)
    def L2NormOfSolution(self, *args): return _Solution.Solution_L2NormOfSolution(self, *args)
    def projectOntoMesh(self, *args): return _Solution.Solution_projectOntoMesh(self, *args)
    def energyErrorTotal(self): return _Solution.Solution_energyErrorTotal(self)
    def setWriteMatrixToFile(self, *args): return _Solution.Solution_setWriteMatrixToFile(self, *args)
    def setWriteMatrixToMatrixMarketFile(self, *args): return _Solution.Solution_setWriteMatrixToMatrixMarketFile(self, *args)
    def setWriteRHSToMatrixMarketFile(self, *args): return _Solution.Solution_setWriteRHSToMatrixMarketFile(self, *args)
    def mesh(self): return _Solution.Solution_mesh(self)
    def bc(self): return _Solution.Solution_bc(self)
    def rhs(self): return _Solution.Solution_rhs(self)
    def ip(self): return _Solution.Solution_ip(self)
    def setBC(self, *args): return _Solution.Solution_setBC(self, *args)
    def setRHS(self, *args): return _Solution.Solution_setRHS(self, *args)
    def setIP(self, *args): return _Solution.Solution_setIP(self, *args)
    def save(self, *args): return _Solution.Solution_save(self, *args)
    __swig_getmethods__["load"] = lambda x: _Solution.Solution_load
    if _newclass:load = staticmethod(_Solution.Solution_load)
    def saveToHDF5(self, *args): return _Solution.Solution_saveToHDF5(self, *args)
    def loadFromHDF5(self, *args): return _Solution.Solution_loadFromHDF5(self, *args)
    __swig_destroy__ = _Solution.delete_Solution
    __del__ = lambda self : None;
Solution_swigregister = _Solution.Solution_swigregister
Solution_swigregister(Solution)

def Solution_solution(*args):
  return _Solution.Solution_solution(*args)
Solution_solution = _Solution.Solution_solution

def Solution_load(*args):
  return _Solution.Solution_load(*args)
Solution_load = _Solution.Solution_load

class SolutionPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SolutionPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SolutionPtr, name)
    __repr__ = _swig_repr
    def __deref__(self): return _Solution.SolutionPtr___deref__(self)
    def __init__(self): 
        this = _Solution.new_SolutionPtr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Solution.delete_SolutionPtr
    __del__ = lambda self : None;
    def solution(self, *args): return _Solution.SolutionPtr_solution(self, *args)
    def solve(self): return _Solution.SolutionPtr_solve(self)
    def addSolution(self, *args): return _Solution.SolutionPtr_addSolution(self, *args)
    def clear(self): return _Solution.SolutionPtr_clear(self)
    def cubatureEnrichmentDegree(self): return _Solution.SolutionPtr_cubatureEnrichmentDegree(self)
    def setCubatureEnrichmentDegree(self, *args): return _Solution.SolutionPtr_setCubatureEnrichmentDegree(self, *args)
    def L2NormOfSolution(self, *args): return _Solution.SolutionPtr_L2NormOfSolution(self, *args)
    def projectOntoMesh(self, *args): return _Solution.SolutionPtr_projectOntoMesh(self, *args)
    def energyErrorTotal(self): return _Solution.SolutionPtr_energyErrorTotal(self)
    def setWriteMatrixToFile(self, *args): return _Solution.SolutionPtr_setWriteMatrixToFile(self, *args)
    def setWriteMatrixToMatrixMarketFile(self, *args): return _Solution.SolutionPtr_setWriteMatrixToMatrixMarketFile(self, *args)
    def setWriteRHSToMatrixMarketFile(self, *args): return _Solution.SolutionPtr_setWriteRHSToMatrixMarketFile(self, *args)
    def mesh(self): return _Solution.SolutionPtr_mesh(self)
    def bc(self): return _Solution.SolutionPtr_bc(self)
    def rhs(self): return _Solution.SolutionPtr_rhs(self)
    def ip(self): return _Solution.SolutionPtr_ip(self)
    def setBC(self, *args): return _Solution.SolutionPtr_setBC(self, *args)
    def setRHS(self, *args): return _Solution.SolutionPtr_setRHS(self, *args)
    def setIP(self, *args): return _Solution.SolutionPtr_setIP(self, *args)
    def save(self, *args): return _Solution.SolutionPtr_save(self, *args)
    def load(self, *args): return _Solution.SolutionPtr_load(self, *args)
    def saveToHDF5(self, *args): return _Solution.SolutionPtr_saveToHDF5(self, *args)
    def loadFromHDF5(self, *args): return _Solution.SolutionPtr_loadFromHDF5(self, *args)
SolutionPtr_swigregister = _Solution.SolutionPtr_swigregister
SolutionPtr_swigregister(SolutionPtr)

# This file is compatible with both classic and new-style classes.


