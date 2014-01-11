
# Compile gitg


Build de la librairie githut libgit2-0

Pour compiler
mkdir build && cd build
cmake ..

//cmake --build .

Pour installer
cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local
sudo cmake --build . --target install


./configure CPPFLAGS="-I/home/acassaigne/Downloads/libgit2/include" CFLAGS="-I/home/acassaigne/Downloads/libgit2/include"
make

[ 23%] Built target git2
[100%] Built target libgit2_clar
Install the project...
-- Install configuration: "Debug"
-- Installing: /usr/local/lib/libgit2.so.0.20.0
-- Installing: /usr/local/lib/libgit2.so.0
-- Installing: /usr/local/lib/libgit2.so
-- Installing: /usr/local/lib/pkgconfig/libgit2.pc
-- Installing: /usr/local/include/git2
-- Installing: /usr/local/include/git2/transport.h
-- Installing: /usr/local/include/git2/filter.h
-- Installing: /usr/local/include/git2/revparse.h
-- Installing: /usr/local/include/git2/trace.h
-- Installing: /usr/local/include/git2/types.h
-- Installing: /usr/local/include/git2/oid.h
-- Installing: /usr/local/include/git2/object.h
-- Installing: /usr/local/include/git2/attr.h
-- Installing: /usr/local/include/git2/buffer.h
-- Installing: /usr/local/include/git2/refspec.h
-- Installing: /usr/local/include/git2/notes.h
-- Installing: /usr/local/include/git2/pack.h
-- Installing: /usr/local/include/git2/signature.h
-- Installing: /usr/local/include/git2/indexer.h
-- Installing: /usr/local/include/git2/push.h
-- Installing: /usr/local/include/git2/blame.h
-- Installing: /usr/local/include/git2/branch.h
-- Installing: /usr/local/include/git2/status.h
-- Installing: /usr/local/include/git2/strarray.h
-- Installing: /usr/local/include/git2/remote.h
-- Installing: /usr/local/include/git2/version.h
-- Installing: /usr/local/include/git2/diff.h
-- Installing: /usr/local/include/git2/patch.h
-- Installing: /usr/local/include/git2/commit.h
-- Installing: /usr/local/include/git2/errors.h
-- Installing: /usr/local/include/git2/common.h
-- Installing: /usr/local/include/git2/tag.h
-- Installing: /usr/local/include/git2/graph.h
-- Installing: /usr/local/include/git2/clone.h
-- Installing: /usr/local/include/git2/inttypes.h
-- Installing: /usr/local/include/git2/submodule.h
-- Installing: /usr/local/include/git2/stdint.h
-- Installing: /usr/local/include/git2/threads.h
-- Installing: /usr/local/include/git2/revert.h
-- Installing: /usr/local/include/git2/blob.h
-- Installing: /usr/local/include/git2/refs.h
-- Installing: /usr/local/include/git2/net.h
-- Installing: /usr/local/include/git2/odb.h
-- Installing: /usr/local/include/git2/reflog.h
-- Installing: /usr/local/include/git2/tree.h
-- Installing: /usr/local/include/git2/refdb.h
-- Installing: /usr/local/include/git2/checkout.h
-- Installing: /usr/local/include/git2/merge.h
-- Installing: /usr/local/include/git2/repository.h
-- Installing: /usr/local/include/git2/stash.h
-- Installing: /usr/local/include/git2/reset.h
-- Installing: /usr/local/include/git2/revwalk.h
-- Installing: /usr/local/include/git2/index.h
-- Installing: /usr/local/include/git2/ignore.h
-- Installing: /usr/local/include/git2/cred_helpers.h
-- Installing: /usr/local/include/git2/sys
-- Installing: /usr/local/include/git2/sys/filter.h
-- Installing: /usr/local/include/git2/sys/commit.h
-- Installing: /usr/local/include/git2/sys/refs.h
-- Installing: /usr/local/include/git2/sys/reflog.h
-- Installing: /usr/local/include/git2/sys/refdb_backend.h
-- Installing: /usr/local/include/git2/sys/repository.h
-- Installing: /usr/local/include/git2/sys/index.h
-- Installing: /usr/local/include/git2/sys/config.h
-- Installing: /usr/local/include/git2/sys/odb_backend.h
-- Installing: /usr/local/include/git2/config.h
-- Installing: /usr/local/include/git2/message.h
-- Installing: /usr/local/include/git2/pathspec.h
-- Installing: /usr/local/include/git2/odb_backend.h
-- Installing: /usr/local/include/git2.h
