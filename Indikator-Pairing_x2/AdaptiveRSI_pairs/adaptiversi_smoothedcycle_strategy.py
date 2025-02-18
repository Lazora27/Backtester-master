import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SmoothedCycle': 1.0
        })
    )
