with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "website";

  buildInputs = with pkgs; [
    python3
  ] ++ (with pkgs.python3Packages; [
    pelican
    markdown
    webassets
  ]);
}
