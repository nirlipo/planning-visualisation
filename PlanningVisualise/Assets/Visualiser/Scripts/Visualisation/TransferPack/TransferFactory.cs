using System;
using TransferPack.TransferItemPack;
using Visualiser;

namespace TransferPack {
   internal static class TransferFactory {

      public static ITransferItem CreateTransferItem(VisualSolutionObject argVisualSolutionObject) {
         switch ((TransferType)argVisualSolutionObject.transferType) {
            case TransferType.FadeIn_FadeOut: return new FadeTransferItem();
            case TransferType.LinerMovement: return new LinerTransferItem();
            case TransferType.TwoPhase: return new TwoPhaseTransferItem(argVisualSolutionObject.transferType);
            default:
               throw new ArgumentOutOfRangeException();
         }
      }

   }
}