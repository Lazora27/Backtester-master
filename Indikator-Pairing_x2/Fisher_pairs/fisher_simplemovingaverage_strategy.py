import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
