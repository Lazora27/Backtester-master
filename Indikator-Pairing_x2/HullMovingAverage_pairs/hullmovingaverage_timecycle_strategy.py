import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und TimeCycle
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'TimeCycle': 1.0
        })
    )
