import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'AccelerationBands': 1.0
        })
    )
