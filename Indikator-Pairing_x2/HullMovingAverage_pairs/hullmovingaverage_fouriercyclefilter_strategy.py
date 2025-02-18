import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
