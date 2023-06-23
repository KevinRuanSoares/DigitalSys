import { api } from '../settings';

export interface ProposlFieldInterface {
    unique_id: string;
    name: string;
    required: boolean;
    field_type: "DATE" | "TEXT" | "NUMBER";
    value: any| undefined;
}

export interface ProposalCreateInterface {
    proposal_field: string;
    value: string;
}

export const ProposalService = {
    async getProposalFields(): Promise<ProposlFieldInterface[]> {
        try {
            const url = 'proposal/fields';
            const { data } = await api.get(url);
            return data;
        } catch (error) {
            console.error(error);
            return [];
        }
    },

    async createProposal(createProposalModel: ProposalCreateInterface[]) {
        try {
          const url = 'proposal/';
    
          const { status } = await api.post(url, createProposalModel);
    
          if (status === 200) return true;
          return false;
        } catch (error: any) {
          console.log(error)
          return false;
        }
      },
};
