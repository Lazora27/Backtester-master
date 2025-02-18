import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'EhlersDecycler': 1.0
        })
    )
