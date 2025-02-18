import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und BarStrength
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'BarStrength': 1.0
        })
    )
