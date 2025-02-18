import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AdaptiveATR': 1.0
        })
    )
