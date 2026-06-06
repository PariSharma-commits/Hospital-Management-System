import { useEffect, useState } from "react";
import { getAppointments } from "./services/api";
import "./index.css";

import { FaUserMd, FaCalendarAlt, FaUsers, FaRupeeSign } from "react-icons/fa";
import { FiSearch } from "react-icons/fi";

function App() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    getAppointments().then(setAppointments);
  }, []);

  return (
    <div className="app">

      {/* SIDEBAR */}
      <div className="sidebar">
        <h2 className="logo">Medix</h2>
        <ul>
          <li className="active">Dashboard</li>
          <li>Appointments</li>
          <li>Patients</li>
          <li>Doctors</li>
        </ul>
      </div>

      {/* MAIN */}
      <div className="main">

        {/* HEADER */}
        <div className="header">
          <div className="search-box">
            <FiSearch />
            <input placeholder="Search..." />
          </div>
          <button className="primary-btn">+ New</button>
        </div>

        {/* STATS */}
        <div className="cards">
          <div className="stat-card">
            <FaUserMd />
            <div>
              <p>Doctors</p>
              <h3>12</h3>
            </div>
          </div>

          <div className="stat-card">
            <FaCalendarAlt />
            <div>
              <p>Appointments</p>
              <h3>28</h3>
            </div>
          </div>

          <div className="stat-card">
            <FaUsers />
            <div>
              <p>Patients</p>
              <h3>15</h3>
            </div>
          </div>

          <div className="stat-card">
            <FaRupeeSign />
            <div>
              <p>Revenue</p>
              <h3>₹45K</h3>
            </div>
          </div>
        </div>

        {/* MAIN GRID */}
        <div className="content-grid">

          {/* BIG PANEL */}
          <div className="appointments-panel">
            <h3>Appointments</h3>

            {appointments.map((a, index) => (
              <div className="appointment-card" key={index}>
                <div className="left">
                  <h4>{a[1]}</h4>
                  <p>{a[2]}</p>
                  <span>{a[3]} • {a[4]}</span>
                </div>

                <div className="right">
                  <div className="status">{a[5]}</div>
                </div>
              </div>
            ))}
          </div>

          {/* SIDE PANEL */}
          <div className="side-panel">
            <h3>Overview</h3>
            <div className="mini-card">+12% growth</div>
            <div className="mini-card">Peak: 11 AM</div>
            <div className="mini-card">Load: Medium</div>
          </div>

        </div>

      </div>
    </div>
  );
}

export default App;