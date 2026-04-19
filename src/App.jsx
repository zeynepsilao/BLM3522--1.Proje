import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [personeller, setPersoneller] = useState([]);
  const [form, setForm] = useState({ id: '', ad: '', soyad: '', departman: '' });

  const API_URL = 'http://13.58.107.245:5000/personel';

  const verileriGetir = async () => {
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      setPersoneller(data);
    } catch (error) {
      console.error("Veri çekme hatası:", error);
    }
  };

  useEffect(() => {
    verileriGetir();
  }, []);

  const personelEkle = async (e) => {
    e.preventDefault();
    try {
      await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      });
      setForm({ id: '', ad: '', soyad: '', departman: '' });
      verileriGetir();
    } catch (error) {
      console.error("Ekleme hatası:", error);
    }
  };

  const personelSil = async (id) => {
    try {
      await fetch(`${API_URL}/${id}`, {
        method: 'DELETE'
      });
      verileriGetir();
    } catch (error) {
      console.error("Silme hatası:", error);
    }
  };

  return (
    <div className="container">
      <h2>Personel Takip Sistemi</h2>
      
      {/* Ekleme Formu */}
      <form onSubmit={personelEkle} className="add-form">
        <div className="input-group">
          <label>ID</label>
          <input type="text" value={form.id} onChange={e => setForm({...form, id: e.target.value})} required />
        </div>
        <div className="input-group">
          <label>Ad</label>
          <input type="text" value={form.ad} onChange={e => setForm({...form, ad: e.target.value})} required />
        </div>
        <div className="input-group">
          <label>Soyad</label>
          <input type="text" value={form.soyad} onChange={e => setForm({...form, soyad: e.target.value})} required />
        </div>
        <div className="input-group">
          <label>Departman</label>
          <input type="text" value={form.departman} onChange={e => setForm({...form, departman: e.target.value})} required />
        </div>
        <button type="submit" className="add-btn">Ekle</button>
      </form>

      {/* Personel Listesi Tablosu */}
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Ad</th>
              <th>Soyad</th>
              <th>Departman</th>
              <th>İşlem</th>
            </tr>
          </thead>
          <tbody>
            {personeller.map(personel => (
              <tr key={personel.id}>
                <td>{personel.id}</td>
                <td>{personel.ad}</td>
                <td>{personel.soyad}</td>
                <td>{personel.departman}</td>
                <td>
                  <button onClick={() => personelSil(personel.id)} className="delete-btn">Sil</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;