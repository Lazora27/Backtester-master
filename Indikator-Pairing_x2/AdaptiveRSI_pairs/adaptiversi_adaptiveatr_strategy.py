import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'AdaptiveATR': 1.0
        })
    )
