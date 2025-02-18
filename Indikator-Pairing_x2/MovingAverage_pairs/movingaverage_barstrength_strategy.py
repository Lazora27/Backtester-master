import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und BarStrength
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'BarStrength': 1.0
        })
    )
