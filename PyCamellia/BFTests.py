import BF
import VarFactory
import Var
import LinearTerm
import Function
import unittest
import PoissonFormulation

class Tests(unittest.TestCase):ls

"""Test the method testName()"""
def testTestName(self):
	


	vf = VarFactory.VarFactory();
	myVar = vf.testVar("identify me 1", 1);
	myVar2 = vf.testVar("identify me 2", 1);
	i = myVar2.ID();
	
	bf = BF.BF(vf);
	self.assertEqual(bf.testName(i), "identify me 2", "testName()");

def testTrialName(self):
	vf = VarFactory.VarFactory();
	myVar = vf.fieldVar("identify me");
	myVar2 = vf.fieldVar("identify me 2");
	i = myVar2.ID();

	bf = BF.BF(vf);
	self.assertEqual(bf.trialName(i), "identify me 2", "trialName()");


"""Test the method """
def testAddTerm(self):


f = Function.Function_xn(1);
g = Function.Function_yn(1);
vf = VarFactory.VarFactory();
u = vf.fieldVar("field");
v = vf.testVar("test", 7);

lt = 1.0 * u;
lt2 = 1.0 * v;
	

bf = BF.BF(vf);

	


	#FunctionPtr
h = lt.evaluate({
		u.ID() : f
		});



        bf.addTerm(lt, lt2);
	h.evaluate(5, 6);

	bf = BF.BF(VarFactory.VarFactory());
	bf.addTerm(lt, lt2);



def testIsFluxOrTrace(self):
	vf = VarFactory.VarFactory();
	myVar = vf.fluxVar("identify me");
	myVar2 = vf.traceVar("hey");
	myVar3 = vf.fieldVar("hi");
	i = myVar.ID();
	j = myVar2.ID();
	k = myVar3.ID();

	bf = BF.BF(vf);
	self.assertEqual(bf.isFluxOrTrace(i), True, "test isFluxOrTrace");
	self.assertEqual(bf.isFluxOrTrace(j), True, "test isFluxOrTrace");
	self.assertEqual(bf.isFluxOrTrace(k), False, "test isFluxOrTrace");
	
	




	
