with open("requirements.txt") as myFile:
  pkgs = myFile.read()
  pkgs = pkgs.splitlines()

  for pkg in pkgs:
      print(pkg.split('==')[0])