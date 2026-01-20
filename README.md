# Pixlate

Turn photos into abstract art.

https://github.com/user-attachments/assets/3f3885c3-b7c4-4240-9bb9-1df03461941f

## Installation

Recommended (modules-aware, Go 1.18+):

```
go install github.com/arnabjena007/pixlate/cmd/pix@latest
```

This installs the `pix` binary into your `GOBIN` (or `$HOME/go/bin` by default). Make sure that directory is in your `PATH`.

Build from source:

```
git clone https://github.com/arnabjena007/Pixlate.git
cd Pixlate
go build ./cmd/pix
# then run:
./pix -in picture.jpg
```

## Usage

Run it like so (minimal):

```
pix -in picture.jpg
```

Run with output, size, or generate multiple variations:

```
pix -in picture.jpg -out pix.output.png -width 800 -height 800
pix -in picture.jpg -sweep
pix -in picture.jpg -variations 4
```

## Flags

The command supports the following flags (see `pix -h` for detailed help):

- `-in` (required): input image path or URL
- `-out`: output image path
- `-width`, `-height`: dimensions of the output
- `-white-percent`, `-colorsort`, `-random`, `-reverse`
- `-sweep`, `-random-seed`, `-variations`
- `-compress`: png compression level
- `-seeds`: seed positions (e.g. "x y x y ...")

## Notes

- The README previously recommended `go get -u ...`; modern Go modules usage prefers `go install ...@latest` for installing binaries. `go get` for installing binaries is deprecated in newer Go versions.
- Recommend using Go 1.18+ for best compatibility with module behavior.
- If you need any help updating the README further or opening a PR with code fixes (I found a couple of small issues in cmd/pix/main.go), I can prepare that for you.