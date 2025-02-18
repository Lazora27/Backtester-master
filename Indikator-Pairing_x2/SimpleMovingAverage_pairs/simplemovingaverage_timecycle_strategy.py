import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'TimeCycle': 1.0
        })
    )
