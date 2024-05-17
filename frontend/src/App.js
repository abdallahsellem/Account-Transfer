
import React from 'react';
import { BrowserRouter , Route, Routes, Link } from 'react-router-dom';
import ImportCsv from './components/ImportCsv';
import ListAllAccounts from './components/ListAllAccounts';
import AccountDetails from './components/AccountDetails';
import TransferFunds from './components/TransferFunds';

function App() {
  return (
    <BrowserRouter>

      <div>
        <nav>
          <ul>
            <li><Link to="/">Import CSV</Link></li>
            <li><Link to="/accounts">List Accounts</Link></li>
            <li><Link to="/account-details">Account Details</Link></li>
            <li><Link to="/transfer-funds">Transfer Funds</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/"  element={<ImportCsv></ImportCsv>} />
          <Route path="/accounts" element={<ListAllAccounts></ListAllAccounts>} />
          <Route path="/account-details" element={<AccountDetails></AccountDetails>} />
          <Route path="/transfer-funds" element={<TransferFunds></TransferFunds>} />
        </Routes>

      </div>
      </BrowserRouter>

  );
}

export default App;
