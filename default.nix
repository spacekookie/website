with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "website";
  src = ./.;

  buildInputs = with pkgs; [
    python3
  ] ++ (with pkgs.python3Packages; [
    pelican
    markdown
    webassets
  ]);

  buildPhase = ''
    runHook preBuild
    make html
    runHook postBuild
  '';

  installPhase = ''
    runHook preInstall
    mv output $out
    runHook postInstall
  '';
}
