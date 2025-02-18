import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und BarStrength
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'BarStrength': 1.0
        })
    )
