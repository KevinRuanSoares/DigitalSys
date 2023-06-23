import React, { useState, useEffect } from 'react';
import { ProposalService, ProposlFieldInterface, ProposalCreateInterface } from './services/proposal-service'
import './style/global.css';
import './style/form.css';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  const [proposalFields, setProposalFields] = useState<ProposlFieldInterface[]>([]);
  async function fetchUserLastVisits() {
    try {
      const response = await ProposalService.getProposalFields();
      
      if (response) setProposalFields(response);
    } catch (error) {
      console.error(error);
    }
  }

  const handleFormChange = (index: number, event:any) => {
    if(proposalFields){
      let data = [...proposalFields];
      data[index]['value'] = event.target.value;
      setProposalFields(data);
    }
  }

  const handleSubmit = async (event:React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    let data:ProposalCreateInterface[] = [];
    proposalFields?.map(proposalField => {
      data.push({
        proposal_field: proposalField.unique_id,
        value: proposalField.value
      });
    })
    const response = await ProposalService.createProposal(data);
    if(response){
      fetchUserLastVisits();
      toast.success("Proposta enviada com sucesso! 😊️")
    }else{
      toast.error("Não foi possível enviar sua proposta. 😔")
    }
  };

  useEffect(() => {
    fetchUserLastVisits()
  }, [])

  return (
    <>
      <ToastContainer />
      <div className='form-container'>
        <h1>Propostas de Empréstimo Pessoal</h1>
        <form onSubmit={handleSubmit}>
          {proposalFields?.map((proposalField, index) => (
            <div className='input-container' key={index}>
              <label htmlFor="firstName">{proposalField.name}</label>
              <input
                type={proposalField.field_type}
                id={proposalField.unique_id}
                name={proposalField.unique_id}
                required={proposalField.required}
                placeholder={proposalField.name}
                onChange={event => handleFormChange(index, event)}
                value={proposalField.value ? proposalField.value : ''}
              />
            </div>
          ))}
          <button type="submit" disabled={proposalFields?.length === 0}>Enviar</button>
        </form>
      </div>
    </>
  )
}

export default App
