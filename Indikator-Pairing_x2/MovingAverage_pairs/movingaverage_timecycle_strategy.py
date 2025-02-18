import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'TimeCycle': 1.0
        })
    )
