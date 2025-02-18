import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'SmoothedCycle': 1.0
        })
    )
