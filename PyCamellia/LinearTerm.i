%module LinearTerm
%{
#include "LinearTerm.h"
%}

%include "std_string.i"
%include "std_map.i"

namespace std {
  %template(MapIntToFunction) map<int,FunctionPtr>;
}

using namespace std;

class LinearTerm {
public:
  LinearTerm();
  const set<int> & varIDs();
  VarType termType();
  FunctionPtr evaluate(std::map< int, FunctionPtr> &functionMap);
  int rank();
  string displayString();

 %extend {
    FunctionPtr evaluate(const map<int, FunctionPtr> &functionMap) {
      map<int, FunctionPtr> functionMapCopy = functionMap;
      return self->evaluate(functionMapCopy);
    }
  }

 };

class LinearTermPtr{
public:
  LinearTerm* operator->();
 
  %extend {
    LinearTermPtr __add__(LinearTermPtr a){
      return *self + a;
    }

    LinearTermPtr __add__(VarPtr v){
      return *self + v;
    }

    LinearTermPtr __radd__(VarPtr v){
      return *self + v;
    }
    /**
       This needs to be added to Var.i in order to work
    LinearTermPtr __rmul__(VarPtr v) {
      return *self * v;
    }
    **/
    LinearTermPtr __sub__() { 
      return - *self;
    }

    LinearTermPtr __sub__(VarPtr v) { 
      return *self - v;
    }

    LinearTermPtr __rsub__(VarPtr v) { 
      return v - *self;
    }

    LinearTermPtr __sub__(LinearTermPtr a) { 
      return *self - a;
    }

  }





};
    //for FunctionPtr and VarPtr without linear term
    //add in the Function and Var .i files
    //VarPtr and double




