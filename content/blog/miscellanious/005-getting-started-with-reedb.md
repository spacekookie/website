Title: Hacking on Reedb
Category: Blog
Date: 2016-03-14 10:43
Tags: Dev Diary, Reedb

So...it's been a while :) Exams are over, code has been written, bugs have been fixed, frustrations have been had. Terrible christmas gifts have been sold off on ebay and found a new owner with a misguided sense of style. I've also gone a bit mad with one of my other projects: The Christmas bauble. As you might recall it started as a harmless joke to learn KiCAD, ended up actually being manufactured (I never saw that bonus from dirtypcb for mentioning them a lot :c) and has now gone into planning phase for Revision B. 

![Reedb Banner](/images/reedb_banner.png  "Reedb Banner")

But more on that later. I'm back, in the spring with new energy and drive. To talk to you about Reedb (yet again).

With `0.12` coming closer and closer to being a reality I wanted to quickly draft up something how to interact with Reedb. The API is basically stable at this point and while the C-binding isn't quite done the C++ interface is ready to be used (and almost actually hooked up :) ).


### Initialising a context

Getting started with reedb requires a context which holds a bunch of information about what vaults exist, what tokens haven been scoped, users active, watchdogs, etc. etc.

In addition to that there are vault interfaces that get attached to a context that can then actually interact with vaults. This way different vaults can get handled by different interfaces that are completely separated from each other.

```C++
reedb *rdb = new reedb();
rdb->set_os(LINUX);
rdb->set_distro(SYSTEM_D);
rdb->set_verbose(true);
rdb->finalise();
```

The OS and sitro flags determine what configuration paths and formats are specified as well as how to launch reedb at system startup (if such a behaviour is wanted/ set up).

After defining all the parameters required or wanted to initialise the Reedb context call finalise to make it official and make the context usable. Before `finalise()` is called, trying to access other functions via the context will result in an error being thrown.

### Vault interfaces

So after having a Reedb context you have to register a vaults interface to it. Multiple interfaces can be registered and separated which means that certain vaults can be accessed that require different settings (for example a minimum passphrase length). Generally it just offers more flexibility to the developers.

```C++
rdb_vaults *v = new rdb_vaults();
rdb->register_vinterface(v);

vault_meta meta = v->create("fancy_vault", "~/Documents/", "MyD0gisnot!mypassword!"); // P.S. I don't have a dog :)
```

The create function will generate a key, encrypt the Master key with the provided passphrase and dump it to disk. In addition a folder structure and configuration is written. The config is mostly future proofing - none of the values are actually currently used. But it will hold information about zones, users and cipher modes in the future.

---

After creating a vault you still need to authenticate on it. The unencrypted key might still be held in RAM (in secure memory that is) but just because you created a vault doesn't automaticaly mean you have access to it. So after calling `create` you need to call:

```C++
// A token is malloced for you in secmem. Do not free it yourself. Let Reedb do it for you!
rdb_token *token = v->authenticate(meta.id, "MyD0gisnot!mypassword!");
```

You need the UUID from the interface we are addressing the vault via - we can find the UUID in the vault_meta we were handed during creation. Alternatively we can ask the vaults interface.

From the docs:
> A UUID is provided from the management wrapper and isn't stored in the vault itself. A vault doesn't care about its own ID, nor does it even know it has one.
>
> Do not try to hard-code UUIDs into your program as they might be non-persistent across runtimes.

Authentication only takes the ID and passphrase at the moment. However a user-auth function will be added in at least the next version. Both return a token that will be required for **every** operation that follows.

And that's it...you can now interact with your shiny new Reedb Vault :)

```C++
std::string file_id = "Reedb.org";
map<std::string*, std::string*> content();
content["Username"] = "Peter Pan";
content["Passphrase"] = "flower123";

/* Then take all that data and insert it */
v->insert(meta.id, token, &file_id, &content); // Takes the pointer to a content map to save memory during inserts.
```

As you can see you need a vault-id and a token to even be allowed to the next step. Then to insert a piece of data you need to give it a name. Reedb is object-oriented which means that every dataset has a name and is an "object" on the FS ( Blockdevice mode is in planning :) ). So from that day on your piece of data will be available if you query for "Reedb.org".

```C++
map<std::string*, file_meta*> data;
data = query_file(meta.id, token, "Reedb.org");
```

That will put a query return into your map. A query return isn't quite data. It's basically a name of a data-set mapped to it's head. A file head contains a bunch of metadata that isn't exactly deemed "important". Like it's name, a category, some tags and whatever else you might want to save in there.
In fact you can extend header fields at will.

```C++
map<std::string*, std::string*> meta_delta();
// ...
v->migrate_headers(&meta_delta);
```

From the docs (again):

> A meta_delta is the name of a meta-field that should be inserted mapped to its type in a std::map<?,?>. 
> If a meta should be removed set the type to "-1".
>
> When removing meta fields from active vaults data needs to be migrated via rdb_meta_migr(...). Also be aware that removing active meta fields can cause terrible memory corruption. Be warned!

A file_meta is exactly that: a vault header. It can be further searched and filtered with RQL (Reedb Query Language) that we will not go into further in this blog post. Just know that it exists :)

*hint hint* `"$CATEGORY: [Social | Website | Online] $TAGS:[Private & Friends] $NAME: ~[Face]"` :)

Deleting, updating files and updating vaults is analogue to what we already saw. Basically you always keep your vault ID and token on you, then provide the interface with some data.

Some of the steps might seem a bit verbose but that's just so that the user (aka developer) gets maximum control over what she is doing with her code. It also allows for more precice error handling - narrowing down the source of the error further for the end-user.

### A tiny last thing

There are two interfaces for Reedb. A C++ and a C one. And you pick which one you want to use by either doing

```C++
#include<reedb/core.hpp>
```

or 
```C
#include<reedb/core.h>
```

The C Interface is pretty much analogue to the C++ one (with obvious slight differences).

```C
vault_meta *meta;
rdb_vaults *vaults = rdb->create(&meta, ...);
```

That's it for today. I hope this article gave you a quick introduction to the native interface and makes you at least a little curious or excited to work with it :)