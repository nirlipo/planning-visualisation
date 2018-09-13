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

namespace TransferPack.TransferItemPack {
   interface ITransferItem {

      void SetTransfer(VisualStageObject argStageToDisappear, VisualStageObject argStageToAppear);

   }
}