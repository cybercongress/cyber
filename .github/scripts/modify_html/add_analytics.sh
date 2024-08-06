#!/bin/sh

analytics_script="<script>
    const script = document.createElement('script');
    script.src = 'https://metrics.cyb.ai/js/script.hash.js';
    script.setAttribute('data-domain', location.host);
    script.defer = true;
    document.body.appendChild(script);
  </script>"

file="$GITHUB_WORKSPACE/build/index.html"

sed -i "/<\/body>/i\\
$(echo "$analytics_script" | sed 's/$/\\n/' | tr -d '\n')\\
" "$file"


