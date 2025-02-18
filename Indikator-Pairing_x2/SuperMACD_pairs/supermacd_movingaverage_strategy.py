import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MovingAverage
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MovingAverage': 1.0
        })
    )
