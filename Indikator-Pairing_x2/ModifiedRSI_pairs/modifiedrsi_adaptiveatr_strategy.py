import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AdaptiveATR': 1.0
        })
    )
