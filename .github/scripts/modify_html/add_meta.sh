#!/bin/sh

metas=$(cat <<'EOF'
    <meta property="og:title" content="cyber docs">

    <meta name="description" content="cyber docs">
    <meta property="og:description" content="cyber docs">

    <meta property="og:image" content="/static/img/logo.png">
EOF
)

find $GITHUB_WORKSPACE/build -name 'index.html' -exec sh -c '
for file do
  sed "/<\/head>/i\\ $metas" "$file"
done
' sh {} +
