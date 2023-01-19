"""
    > Módulos são Singleton > Importados apenas 1 Vez >Tipo Pragma Once do C++<
    > ImportLib
"""
import importlib
from modulo.utils import pcomment
from modulo import pp,pcomment, pl
import modulo

cc = pcomment('CasaNova')
print('My names is...', __name__)
importlib.reload(modulo)  ## Reloaded