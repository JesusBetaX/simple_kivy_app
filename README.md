## KIVY

MVC 

## Crear instalador

Empaquetar una aplicación simple 

1. Abra su shell de línea de comando.
   
2. Ejecute este comando en la raíz del proyecto:
```markdown
python -m PyInstaller --onefile --name myApp src\main.py
```

3. Abra el archivo **myApp.spec** con su editor favorito y agregue estas líneas al comienzo de la especificación (asumiendo que se usa sdl2, el predeterminado ahora):
```python
from kivy_deps import sdl2, glew
```

3.2 Edite los argumentos del comando **EXE** del mismo archivo.
```python
*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
```
Quedará de esta manera
```python
exe = EXE(pyz, Tree('examples-path\\demo\\touchtracer\\'),
     a.scripts,
     a.binaries,
     a.zipfiles,
     a.datas,
     *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
     upx=True
     name='touchtracer')
```

4. Ahora puede crear el archivo de especificaciones como antes con:
```python
python -m PyInstaller myApp.spec
```

El paquete compilado estará en el directorio **\dist** y constará de un solo archivo ejecutable.