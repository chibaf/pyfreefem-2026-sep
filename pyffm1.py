from pyfreefem import FreeFemRunner

fem_matrix="""
IMPORT "io.edp"
mesh Th=square($N,$N);
fespace Fh1(Th,P1);
varf laplace(u,v)=int2d(Th)(dx(u)*dx(v)+dy(u)*dy(v));
matrix A = laplace(Fh1,Fh1,tgv=-2);

exportMatrix(A);"""

#Get the sparse matrix (scipy csc_matrix format) A:
runner = FreeFemRunner(fem_matrix)
exports = runner.execute({'N':100})
A = exports['A']
print('A=\n',A.todense())
