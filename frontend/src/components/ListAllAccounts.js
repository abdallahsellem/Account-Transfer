
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ListAllAccounts() {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    const fetchAccounts = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/accounts');
        setAccounts(response.data);
      } catch (error) {
        console.error('Failed to fetch accounts', error);
      }
    };

    fetchAccounts();
  }, []);

  return (
    <div>
      <h2>Accounts</h2>
      <ul>
        {accounts.map((account) => (
          <li key={account.id}>{account.owner_name}: ${account.balance}</li>
        ))}
      </ul>
    </div>
  );
}

export default ListAllAccounts;
