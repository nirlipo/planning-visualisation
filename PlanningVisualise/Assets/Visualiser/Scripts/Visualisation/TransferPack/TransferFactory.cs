///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * 
 * Purpose: This file is used to handle transfered dataobjects animation tyype and generate functionality of thier properties accordingly
 * Authors: Tom, Collin, Hugo and Sharukh
 * Date: 14/08/2018
 * Reviewers: Sharukh, Gang and May
 * Review date: 10/09/2018
 * 
 * /
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  */

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