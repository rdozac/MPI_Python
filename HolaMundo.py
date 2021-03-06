#!/usr/bin/env python
"""Hola Mundo en Paralelo"""

from mpi4py import MPI
import sys
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
sys.stdout.write("Hola, Mundo! Soy el Core %d de %d en el %s.\n" % (rank, size, name))
