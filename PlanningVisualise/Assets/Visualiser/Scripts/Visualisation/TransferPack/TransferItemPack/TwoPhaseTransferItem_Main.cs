

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * 
 * Purpose: The file has fucntionality to set the transfer object type
 * Authors: Tom, Collin, Hugo and Sharukh
 * Date: 14/08/2018
 * Reviewers: Sharukh, Gang and May
 * Review date: 10/09/2018
 * 
 * /
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  */


using Visualiser;

namespace TransferPack.TransferItemPack
{
    internal partial class TwoPhaseTransferItem : ITransferItem
    {

        private IDisappearItem disappearItem;
        private IAppearItem appearItem;
        //TODO
        public TwoPhaseTransferItem(int argTransferType)
        {
            //disappearItem = XXXXXX;
            //appearItem = XXXXXX;
        }
        //TODO
        public void SetTransfer(VisualStageObject argStageToDisappear, VisualStageObject argStageToAppear)
        {
            throw new System.NotImplementedException();
        }

    }
}