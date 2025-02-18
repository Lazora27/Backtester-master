import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
