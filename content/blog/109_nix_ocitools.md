Title: ociTools in NixOS
Category: Blog
Date: 2019-09-09 18:00
Tags: /dev/diary, NixOS, Virtualisation

With the release of NixOS 19.09 any second now, I thought I wanted to
blog about something that I've been working on, that [recently][0]
made it into `master`, and thus the new stable channel. So I thought,
why not blog about it a bunch.

[0]: https://github.com/NixOS/nixpkgs/pull/56411

## What are OCI tools?

[Open Container Initiative][1] (or OCI) produced a spec that
standardised what format containers should use. It is implemented by a
bunch of runners, such as `runc` (the Docker/ standard Kubernetes
backend) and `railcar` (more to that later) and outlines in exactly
what format a containers metadata and filesystem are to be stored, so
to achieve the largest possible reusability.

[1]: https://www.opencontainers.org/

The spec is pretty [long][3] and in some places not very
great. There's even a [blog post][4] from Oracle, talking about how
implementing an OCI runner in Rust made them find bugs in the
specification.

[3]: https://github.com/opencontainers/runtime-spec
[4]: https://blogs.oracle.com/developers/building-a-container-runtime-in-rust

## What are ociTools?

So now the question is, what does that have to do with
NixOS/nixpkgs. The answer is simple: I wanted to be able to
containerise single applications on my server, without requiring a
container daemon (such as docker) or relying on externally built
"Docker containers" from a registry.

So, `ociTools.buildContainer` was recently merged into `nixpkgs/master`, allowing you to do exactly that. It's usage is farely
straight forward

```nix
with pkgs; ociTools.buildContainer {
  args = [
    (writeShellScript "run.sh" ''
      ${hello}/bin/hello -g "Hello from OCI container!"
    '').outPath
  ];
}
```

The `args` parameter refers to a list of paths and arguments that are
handed to a container runner to run as init. In this case it's
creating a shell script with some commands in it, then getting the
output derivation path. Alternatively, if you only want to run a
single application, you can pass it `<package>.outPath` directly
instead.

There's other options available, such as the `os`, `arch` and
`readonly` flags (which aren't very interesting and have sane
defaults). Additionally to that there's `mounts`.

Simply specify any bind-mount you wish to setup at container init in a
similar way you would describe your filesystem with `nix` already:

```nix
with pkgs; ociTools.buildContainer {
  args = [
    (writeShellScript "run.sh" ''
      ${hello}/bin/hello -g "Hello from OCI container!"
    '').outPath
  ];
  mounts."/data" = {
    source = "/var/lib/mydata";
  };
}
```

## Railcar + ociTools

So that's all nice and good. But what about actually running these
containers. Well, as I previously said I didn't want to have a
dependency on a management daemon such as `docker`. Instead, I also
added a module for the afromentioned `railcar` container runner
(Oracle please merge my PR, thank you).

It wraps very cleanly around `ociTools` and generates `systemd` units
to start containers, restarting them if they crash. This way you can
express applications purely in `nix`, give them access to only the
things they need, and be sure that their configuration is in line with
the rest of your system rebuild.

```nix
services.railcar = {
  enable = true;
  containers = {
    "hello" = {
      cmd = ''
        ${pkgs.hello}/bin/hello -g "Hello railcar!"
      '';
    };
  };
};
```

The metadata interface for `mounts`, etc is the same for `railcar` as
for `ociTools`.

Anyway, I hope you enjoy. There is definitely things to improve,
especially considering the vastness of the OCI spec. Plus, at the
moment `ociTools` does require a bunch of manual setup work for an
application to function, if it, say, runs a webserver. It would be
cool if some NixOS modules could be re-used to make this configuration
easier. But I'm sure someone else is gonna have fun figuring that out.
