import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
