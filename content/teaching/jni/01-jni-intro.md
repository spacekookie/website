Title: 01. (Java Native Access) The basics
Category: JNI
Tags: Java, Tutorial, Programming
Slug: 01-jni-the-idea-foreign-function-interfaces
Status: draft

Regular readers of my blog (or listeners of my afk ramblings) will know that I like Java. I'm sometimes not quite sure why but there it goes, let's just assume that as an axiome for a second.

Java is pretty damn good at a lot of stuff. It compiles to a high performant byte-code and it's JIT compiler is smart, fault-tolerant and self optimising. It has a plethora of libraries and toolkits to choose from and making nearly anything is pretty damn if you don't mind writing a verbose language or [cheating](https://projectlombok.org/) a bit.

Then so far so good. What is this about then? Well...many things that Java doesn't do in it's standard lib you can still do. And it's something too many people to know about. For good reasons. Fault tolerance and optimisation on the side of the JIT compiler goes out the window and existing documentation is lackluster at best, in most cases outdated by decades at this point. Java is (among other things) an enterprise language and the tech hipsters have *looong* moved on from it. And so have people writing guides about it.

That is about to change (to some small extent)


### What is JNI?

The **J**ava **N**ative **I**nterface is a foreign-function-interface to the JVM, the virtual machine and JIT compiler environment that all Java code runs in. It allows you to write C/C++ code that is called by your existing Java project and even make calls *back* into your java code for callbacks (for example for logging).

It features a very low overhead, practically non-existant safety checking and allows for pretty performant Java-native interop. In fact, switching from the Java context to a native function context only takes [a few nanoseconds](http://stackoverflow.com/a/13977914/2443595). After that you get the raw performance of native code and all the beautiful header bindings that come with that.

Unfortunately setting this up isn't trivial and outdated documentation/ tutorials, that ignore modern build systems, don't make it easier. And while I will get into the nitty-gritty of what you should do/ avoid in the next article (or two), first I want to outline how java-native interop generally works.


### Writing a "native" class

Everything in Java is a class and this is no exception. Thus we first need to provide one that has a few `native` functions that we can then later implement. Other than native functions this class can contain normal java code although I would recommend you don't do that for the sake of readability.

```java

class JniSomething {
    
    static {
        // TODO: Load library
    }

    private long something;

    public native void initSomething(String name, int count);

    public native void doSomething();

    public static native void status(int mode);
}

```

Two things that you should notice

1. We have a static initialiser block which we will later use to load a native library
2. We have a `long` type field in our class which will become important later. For now it shows that "native" classes can have fields just like any other class.

You can also see that we can have static and non-static native functions. Parameters can be primitives and classes although I only demonstrated `String` as a class here (which is a bit of a special case in JNI land)

### Native code generation

We are about a third of the way there. Unfortunately this is where it becomes a little less clean and easy to manage. From our class definition that includes native functions we will now generate a header that we can build native function implementations for.

The tool we will use is called `javah` so make sure it's included in what your operating system packages as java. On most Linux distributions it should come installed with the JDK, on Windows and Mac...I have no idea. Figure it out and e-mail me so I can add it to the article.

Assuming that your "project" structure looks something like this and your current directory is `src`

```
 🚀  (normandy) ~> tree project/
project/
└── src
    └── de
        └── spacekookie
            └── JniSomething.java
```

then you can generate the jni header file in the project root directory as follows

```console
javah -verbose -jni -o ../JniSomething.h de.spacekookie.JniSomething
```

So far so good. You can look at the file now if you want. It's actually pretty ugly code. The function names are designed to *never* clash with anything else because of how Java and C++ have *very* different approaches when it comes to scoping things. The last part of this intro will be writing code that uses these headers to do something in native code.


### Writing & linking native functions

Aaaaand this is where things get really complicated real fast. There are a few things we need to do at this point and none of them are trivial

1. We need to setup our build environment so that we can find the `<jni.h>` utility header
    - Platform specific problems I might add
    - Also very dependant on the build system we might be using later
2. Write and compile the native code that does *something* and make a library (for us that is an `.so` because Linux)
3. Load the library correctly as to not crash the JVM

Easy as pie :)

First things first, we need to find the Java home directory. Again, I can only speak from a Linux perspective. But the `$JAVA_HOME` environment variable was depreciated years ago by most distributions. This might not be the best way to find out but it works.

```bash
# Bash
echo $(dirname $(readlink -f $(which javac)))
```
```fish
# fish
echo (dirname (dirname (readlink -f (which javac))))
```

From the directory we get with these queuries we need to go up one directory and then into a other directory. In the end the path we want to build should look something like this. The second one will obviously be different depending on your platform.

```
/usr/lib/jvm/java-8-openjdk-amd64/bin/../include
/usr/lib/jvm/java-8-openjdk-amd64/bin/../include/linux
```

