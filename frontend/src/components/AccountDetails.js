
import React, { useState } from 'react';
import axios from 'axios';

function AccountDetails() {
  const [accountId, setAccountId] = useState('');
  const [account, setAccount] = useState(null);

  const handleInputChange = (e) => {
    setAccountId(e.target.value);
  };

  const handleFetchAccount = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/api/accounts/${accountId}/`);
      setAccount(response.data);
    } catch (error) {
      console.error('Failed to fetch account details', error);
      setAccount(null);
    }
  };

  return (
    <div>
      <h2>Account Details</h2>
      <input type="text" value={accountId} onChange={handleInputChange} placeholder="Enter account ID" />
      <button onClick={handleFetchAccount}>Get Account Details</button>
      {account && (
        <div>
          <h3> Name: {account.owner_name}</h3>
          <p>Balance: ${account.balance}</p>
        </div>
      )}
    </div>
  );
}

export default AccountDetails;
