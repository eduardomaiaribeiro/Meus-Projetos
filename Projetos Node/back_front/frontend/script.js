document.getElementById('btn-api').onclick = async () => {
  const res = await fetch('/api/hello');
  const data = await res.json();
  document.getElementById('api-response').textContent = data.message;
};
