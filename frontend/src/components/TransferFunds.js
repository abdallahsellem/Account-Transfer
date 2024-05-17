
import React, { useState } from 'react';
import axios from 'axios';

function TransferFunds() {
  const [senderId, setSenderId] = useState('');
  const [receiverId, setReceiverId] = useState('');
  const [amount, setAmount] = useState('');
  const [message, setMessage] = useState('');

  const handleTransfer = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/accounts/transfer/', {
        sender_id: senderId,
        receiver_id: receiverId,
        amount: parseFloat(amount)
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage(error.response.data.error || 'Failed to transfer funds');
    }
  };

  return (
    <div>
      <h2>Transfer Funds</h2>
      <input type="text" value={senderId} onChange={(e) => setSenderId(e.target.value)} placeholder="Sender ID" />
      <input type="text" value={receiverId} onChange={(e) => setReceiverId(e.target.value)} placeholder="Receiver ID" />
      <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount" />
      <button onClick={handleTransfer}>Transfer</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default TransferFunds;
