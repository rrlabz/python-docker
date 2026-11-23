# python-docker
python-3.15.2 docker image

docker buildx build \
    --load \
    -f Dockerfile-slim-v2 \
    -t python-scratch:3.15.2-slim .

curl -sSfL https://get.anchore.io/syft \
  | sudo sh -s -- -b /usr/local/bin

syft python-scratch:3.15.2-slim -o cyclonedx-json=python-scratch-sbom.json

syft python-scratch:3.15.2-slim

curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh \
  | sudo sh -s -- -b /usr/local/bin


trivy image \
  --severity UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL \
  python-scratch:3.15.2-slim


trivy image \
  --format json \
  --output trivy-report.json \
  python-scratch:3.15.2-slim