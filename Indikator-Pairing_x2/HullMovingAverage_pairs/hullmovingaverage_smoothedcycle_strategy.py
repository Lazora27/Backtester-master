import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'SmoothedCycle': 1.0
        })
    )
