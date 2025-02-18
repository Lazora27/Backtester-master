import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'SmoothedCycle': 1.0
        })
    )
