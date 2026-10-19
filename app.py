HTML_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AUTOKARDS</title>
<style>
  :root {
    --bg: #fff3e0;
    --card-bg: #ffffff;
    --accent: #ff8c00;
    --accent-dark: #e67300;
    --text: #3d2000;
    --muted: #a06030;
    --border: #ffc266;
    --input-bg: #ffffff;
    --spec-bg: #fff0d9;
    --modal-overlay-bg: rgba(61, 32, 0, 0.65);
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
  }
  .header { text-align: center; padding: 30px 20px 10px; }
  .logo {
    font-size: 3.5rem;
    font-weight: 900;
    letter-spacing: 4px;
    color: var(--accent);
    text-shadow:
      0 0 4px rgba(255, 179, 71, 0.8),
      0 0 12px rgba(255, 140, 0, 0.6),
      0 0 24px rgba(255, 102, 0, 0.4);
    animation: pulse-glow 2.5s ease-in-out infinite alternate;
  }
  @keyframes pulse-glow {
    from {
      text-shadow:
        0 0 4px rgba(255, 179, 71, 0.8),
        0 0 12px rgba(255, 140, 0, 0.6);
    }
    to {
      text-shadow:
        0 0 6px rgba(255, 179, 71, 1),
        0 0 18px rgba(255, 140, 0, 0.8),
        0 0 30px rgba(255, 102, 0, 0.5);
    }
  }
  .subtitle { color: var(--muted); margin-top: 8px; font-size: 1.1rem; }
  .container { max-width: 1100px; margin: 0 auto; padding: 20px; }
  .cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 20px;
    margin-top: 30px;
  }
  .card {
    background: var(--card-bg);
    border: 2px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 2px 8px rgba(255, 140, 0, 0.15);
  }
  .card:hover {
    transform: translateY(-6px);
    box-shadow: 0 8px 24px rgba(255, 140, 0, 0.35);
  }
  .card img {
    width: 100%;
    height: 160px;
    object-fit: cover;
    display: block;
    background: #ffe8cc;
  }
  .card-body { padding: 12px 16px; }
  .card-name { font-size: 1.2rem; font-weight: 700; color: var(--accent-dark); }
  .card-vin { font-size: 0.8rem; color: var(--muted); margin-top: 4px; letter-spacing: 1px; }
  .stars { margin-top: 6px; color: var(--accent); font-size: 1rem; letter-spacing: 2px; }

  .modal-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: var(--modal-overlay-bg);
    z-index: 1000;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  .modal-overlay.active { display: flex; }
  .modal {
    background: #fffaf0;
    border: 2px solid var(--border);
    border-radius: 20px;
    max-width: 560px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    padding: 24px;
    box-shadow: 0 10px 40px rgba(255, 140, 0, 0.35);
    position: relative;
  }
  .modal-close {
    position: absolute;
    top: 12px;
    right: 16px;
    background: none;
    border: none;
    color: var(--accent);
    font-size: 2rem;
    cursor: pointer;
    line-height: 1;
  }
  .modal h2 { color: var(--accent-dark); margin-bottom: 6px; font-size: 1.6rem; }
  .modal .vin { color: var(--muted); font-size: 0.9rem; margin-bottom: 12px; }
  .modal img {
    width: 100%;
    max-height: 240px;
    object-fit: contain;
    border-radius: 12px;
    margin-bottom: 16px;
    background: #fff0d9;
  }
  .specs { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px; }
  .spec-item {
    background: var(--spec-bg);
    padding: 10px 14px;
    border-radius: 10px;
    border-left: 3px solid var(--accent);
  }
  .spec-label {
    font-size: 0.75rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  .spec-value { font-size: 1.1rem; font-weight: 700; color: var(--text); margin-top: 2px; }

  .admin-bar {
    text-align: center;
    padding: 40px 20px;
    margin-top: 40px;
    border-top: 1px solid var(--border);
  }
  .admin-bar input {
    background: var(--input-bg);
    border: 2px solid var(--border);
    border-radius: 10px;
    padding: 10px 16px;
    color: var(--text);
    font-size: 1rem;
    width: 220px;
    outline: none;
    transition: border-color 0.2s;
  }
  .admin-bar input:focus { border-color: var(--accent); }
  .admin-bar button {
    background: var(--accent);
    border: none;
    border-radius: 10px;
    padding: 10px 24px;
    font-size: 1rem;
    font-weight: 700;
    color: #ffffff;
    cursor: pointer;
    margin-left: 8px;
    transition: box-shadow 0.2s;
  }
  .admin-bar button:hover { box-shadow: 0 0 20px rgba(255, 140, 0, 0.6); }
  .admin-hint { color: var(--muted); font-size: 0.95rem; margin-bottom: 10px; }

  .add-car-btn {
    display: none;
    margin: 24px auto 0;
    background: var(--accent);
    border: none;
    border-radius: 14px;
    padding: 14px 32px;
    font-size: 1.1rem;
    font-weight: 800;
    color: #ffffff;
    cursor: pointer;
    transition: box-shadow 0.2s, transform 0.1s;
  }
  .add-car-btn:hover {
    box-shadow: 0 6px 25px rgba(255, 140, 0, 0.6);
    transform: scale(1.03);
  }
  .add-car-btn.visible { display: block; }

  .form-group { margin-bottom: 14px; }
  .form-group label {
    display: block;
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  .form-group input,
  .form-group select {
    width: 100%;
    background: var(--input-bg);
    border: 2px solid var(--border);
    border-radius: 10px;
    padding: 10px 14px;
    color: var(--text);
    font-size: 1rem;
    outline: none;
  }
  .form-group input:focus,
  .form-group select:focus { border-color: var(--accent); }
  .form-group input[type="file"] { padding: 8px; }

  .submit-btn {
    width: 100%;
    background: var(--accent);
    border: none;
    border-radius: 12px;
    padding: 14px;
    font-size: 1.1rem;
    font-weight: 800;
    color: #ffffff;
    cursor: pointer;
    margin-top: 8px;
    transition: box-shadow 0.2s;
  }
  .submit-btn:hover { box-shadow: 0 4px 20px rgba(255, 140, 0, 0.6); }

  .error-msg { color: #cc0000; font-size: 0.9rem; margin-top: 6px; display: none; }
  .success-msg { color: #008800; font-size: 0.9rem; margin-top: 6px; display: none; }
  .empty-state {
    text-align: center;
    color: var(--muted);
    padding: 60px 20px;
    font-size: 1.1rem;
  }
</style>
</head>
<body>

<div class="header">
  <div class="logo">AUTOKARDS</div>
  <div class="subtitle">Это небольшой проект для автолюбителей — добро пожаловать!</div>
</div>

<div class="container">
  <div id="cardsGrid" class="cards-grid"></div>
  <div id="emptyState" class="empty-state" style="display:none;">
    Пока нет ни одной карточки. Добавьте первую!
  </div>
  <button id="addCarBtn" class="add-car-btn" type="button">➕ Добавить машину</button>
</div>

<div id="viewModal" class="modal-overlay">
  <div class="modal">
    <button class="modal-close" onclick="closeViewModal()">×</button>
    <h2 id="viewName"></h2>
    <div class="vin" id="viewVin"></div>
    <img id="viewImage" src="" alt="">
    <div class="stars" id="viewStars"></div>
    <div class="specs" id="viewSpecs"></div>
  </div>
</div>

<div id="addModal" class="modal-overlay">
  <div class="modal">
    <button class="modal-close" onclick="closeAddModal()">×</button>
    <h2>Добавить машину</h2>
    <form id="addForm" onsubmit="submitCar(event)">
      <div class="form-group">
        <label>Фото машины (вид сбоку)</label>
        <input type="file" id="carImage" accept="image/*" required>
      </div>
      <div class="form-group">
        <label>Название машины</label>
        <input type="text" id="carName" placeholder="Например, Lada Vesta" required>
      </div>
      <div class="form-group">
        <label>Количество звёзд (1–8)</label>
        <input type="number" id="carStars" min="1" max="8" required>
      </div>
      <div class="form-group">
        <label>VIN номер (формат AK-000)</label>
        <input type="text" id="carVin" placeholder="AK-123" pattern="AK-\\d{3}" required>
      </div>
      <div class="form-group">
        <label>Лошадиные силы</label>
        <input type="number" id="carHp" min="0" required>
      </div>
      <div class="form-group">
        <label>Разгон 0–100 (сек)</label>
        <input type="number" id="carAccel" step="0.1" min="0" required>
      </div>
      <div class="form-group">
        <label>Максимальная скорость (км/ч)</label>
        <input type="number" id="carTopSpeed" min="0" required>
      </div>
      <div class="form-group">
        <label>Привод</label>
        <select id="carDrivetrain" required>
          <option value="">— Выберите —</option>
          <option value="FWD">Передний</option>
          <option value="RWD">Задний</option>
          <option value="AWD">Полный</option>
        </select>
      </div>
      <button type="submit" class="submit-btn">Добавить</button>
      <div id="addError" class="error-msg"></div>
      <div id="addSuccess" class="success-msg"></div>
    </form>
  </div>
</div>

<div class="admin-bar">
  <div class="admin-hint">Секретный код</div>
  <div>
    <input type="password" id="secretCode" placeholder="Секретный код">
    <button type="button" onclick="activateAdmin()">Активировать</button>
  </div>
  <div id="adminError" class="error-msg"></div>
</div>

<script>
  const API = '';
  let isAdmin = false;
  let adminCode = '';

  window.addEventListener('error', function(e) {
    console.error('JS Error:', e.message, 'at', e.filename, e.lineno);
  });

  async function loadCars() {
    try {
      const res = await fetch(API + '/api/cars');
      const cars = await res.json();
      const grid = document.getElementById('cardsGrid');
      const empty = document.getElementById('emptyState');
      grid.innerHTML = '';
      if (cars.length === 0) {
        empty.style.display = 'block';
        return;
      }
      empty.style.display = 'none';
      cars.forEach(car => {
        const card = document.createElement('div');
        card.className = 'card';
        card.onclick = () => openViewModal(car);
        const starsStr = '★'.repeat(car.stars) + '☆'.repeat(8 - car.stars);
        card.innerHTML = `
          <img src="${car.image_base64 ? 'data:image/png;base64,' + car.image_base64 : ''}" alt="${car.name}">
          <div class="card-body">
            <div class="card-name">${car.name}</div>
            <div class="card-vin">${car.vin}</div>
            <div class="stars">${starsStr}</div>
          </div>
        `;
        grid.appendChild(card);
      });
    } catch (err) {
      console.error('loadCars failed:', err);
    }
  }

  function openViewModal(car) {
    document.getElementById('viewName').textContent = car.name;
    document.getElementById('viewVin').textContent = 'VIN: ' + car.vin;
    document.getElementById('viewImage').src = car.image_base64 ? 'data:image/png;base64,' + car.image_base64 : '';
    document.getElementById('viewStars').textContent = '★'.repeat(car.stars) + '☆'.repeat(8 - car.stars);
    const drivetrainMap = { FWD: 'Передний', RWD: 'Задний', AWD: 'Полный' };
    document.getElementById('viewSpecs').innerHTML = `
      <div class="spec-item"><div class="spec-label">Л.С.</div><div class="spec-value">${car.horsepower}</div></div>
      <div class="spec-item"><div class="spec-label">0–100 км/ч</div><div class="spec-value">${car.acceleration} с</div></div>
      <div class="spec-item"><div class="spec-label">Макс. скорость</div><div class="spec-value">${car.top_speed} км/ч</div></div>
      <div class="spec-item"><div class="spec-label">Привод</div><div class="spec-value">${drivetrainMap[car.drivetrain] || car.drivetrain}</div></div>
    `;
    document.getElementById('viewModal').classList.add('active');
  }

  function closeViewModal() {
    document.getElementById('viewModal').classList.remove('active');
  }

  async function activateAdmin() {
    const code = document.getElementById('secretCode').value.trim();
    const errEl = document.getElementById('adminError');
    errEl.style.display = 'none';
    if (!code) return;
    try {
      const res = await fetch(API + '/api/admin/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code })
      });
      if (res.ok) {
        isAdmin = true;
        adminCode = code;
        document.getElementById('addCarBtn').classList.add('visible');
        errEl.style.display = 'none';
      } else {
        errEl.textContent = 'Неверный код';
        errEl.style.display = 'block';
      }
    } catch (err) {
      console.error('activateAdmin failed:', err);
      errEl.textContent = 'Ошибка сети';
      errEl.style.display = 'block';
    }
  }

  function openAddModal() {
    if (!isAdmin) {
      console.warn('openAddModal called but isAdmin is false');
      return;
    }
    try {
      document.getElementById('addForm').reset();
      document.getElementById('addError').style.display = 'none';
      document.getElementById('addSuccess').style.display = 'none';
      document.getElementById('addModal').classList.add('active');
    } catch (err) {
      console.error('openAddModal failed:', err);
    }
  }

  function closeAddModal() {
    document.getElementById('addModal').classList.remove('active');
  }

  async function submitCar(e) {
    e.preventDefault();
    const errEl = document.getElementById('addError');
    const sucEl = document.getElementById('addSuccess');
    errEl.style.display = 'none';
    sucEl.style.display = 'none';

    if (!isAdmin || !adminCode) {
      errEl.textContent = 'Сначала активируйте режим администратора';
      errEl.style.display = 'block';
      return;
    }

    const fileInput = document.getElementById('carImage');
    const file = fileInput.files[0];
    if (!file) {
      errEl.textContent = 'Выберите изображение';
      errEl.style.display = 'block';
      return;
    }

    const reader = new FileReader();
    reader.onload = async function() {
      try {
        const base64 = reader.result.split(',')[1];
        const payload = {
          name: document.getElementById('carName').value.trim(),
          stars: parseInt(document.getElementById('carStars').value),
          vin: document.getElementById('carVin').value.trim().toUpperCase(),
          horsepower: parseInt(document.getElementById('carHp').value),
          acceleration: parseFloat(document.getElementById('carAccel').value),
          top_speed: parseInt(document.getElementById('carTopSpeed').value),
          drivetrain: document.getElementById('carDrivetrain').value,
          image_base64: base64,
          admin_code: adminCode
        };

        const res = await fetch(API + '/api/cars', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          sucEl.textContent = 'Машина добавлена!';
          sucEl.style.display = 'block';
          await loadCars();
          setTimeout(closeAddModal, 800);
        } else {
          const data = await res.json();
          errEl.textContent = data.detail || 'Ошибка при добавлении';
          errEl.style.display = 'block';
        }
      } catch (err) {
        console.error('submitCar failed:', err);
        errEl.textContent = 'Ошибка сети';
        errEl.style.display = 'block';
      }
    };
    reader.readAsDataURL(file);
  }

  document.getElementById('addCarBtn').addEventListener('click', function(e) {
    e.preventDefault();
    openAddModal();
  });

  window.addEventListener('click', function(e) {
    if (e.target.classList && e.target.classList.contains('modal-overlay')) {
      e.target.classList.remove('active');
    }
  });

  loadCars();
</script>
</body>
</html>
"""
