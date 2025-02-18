import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MovingAverage
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MovingAverage': 1.0
        })
    )
