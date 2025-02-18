import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
