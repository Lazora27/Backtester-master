import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
