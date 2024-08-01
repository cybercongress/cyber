#!/bin/sh

metas=$(cat <<'EOF'
    <meta property="og:title" content="cyber docs">

    <meta name="description" content="cyber docs">
    <meta property="og:description" content="cyber docs">

    <meta property="og:image" content="/static/img/logo.png">
EOF
)

sed "/<\/head>/i\\ $metas" $GITHUB_WORKSPACE/build/index.html
