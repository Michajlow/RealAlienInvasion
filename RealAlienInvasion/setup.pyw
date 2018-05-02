from cx_Freeze import setup, Executable

includefiles = ['bg.bmp', 'totalship.bmp','enemy2.bmp']

setup(name = 'Alien Attack', 
      version = '1.0', 
      description = 'Whatever',
      options = {'build_exe': {'include_files':includefiles}},
      executables = [Executable(script = 'RealAlienInvasion.pyw')]
      )
