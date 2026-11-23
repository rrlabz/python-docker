# python-docker
python-3.15.2 docker image


# Build the Python 3.15.2 slim image.
docker buildx build \
    --load \
    -f Dockerfile-slim-v2 \
    -t python-scratch:3.15.2-slim .


# Install Syft for SBOM generation.
curl -sSfL https://get.anchore.io/syft \
  | sudo sh -s -- -b /usr/local/bin


# Generate a CycloneDX SBOM and display the image package inventory.
syft python-scratch:3.15.2-slim -o cyclonedx-json=python-scratch-sbom.json


# Display the image package inventory.
syft python-scratch:3.15.2-slim

# Install Trivy for vulnerability scanning.
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh \
  | sudo sh -s -- -b /usr/local/bin


# Scan the image for vulnerabilities and display all severity levels.
trivy image \
  --severity UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL \
  python-scratch:3.15.2-slim


# Save the vulnerability scan results as JSON.
trivy image \
  --format json \
  --output trivy-report.json \
  python-scratch:3.15.2-slim