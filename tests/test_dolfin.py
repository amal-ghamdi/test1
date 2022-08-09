import pytest

def test_dolfin():
    import dolfin as dl
    mesh = dl.UnitSquareMesh(20,20)
    assert(mesh.num_cells()==800)

def test_dolfin_dummy():
    assert(True)

