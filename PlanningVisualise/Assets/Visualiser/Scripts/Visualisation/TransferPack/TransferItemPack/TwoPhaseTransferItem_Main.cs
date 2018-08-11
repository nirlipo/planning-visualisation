using Visualiser;

namespace TransferPack.TransferItemPack {
   internal partial class TwoPhaseTransferItem : ITransferItem {

      private IDisappearItem disappearItem;
      private IAppearItem appearItem;

      public TwoPhaseTransferItem(int argTransferType) {
         //disappearItem = XXXXXX;
         //appearItem = XXXXXX;
      }

      public void SetTransfer(VisualStageObject argStageToDisappear, VisualStageObject argStageToAppear) {
         throw new System.NotImplementedException();
      }

   }
}