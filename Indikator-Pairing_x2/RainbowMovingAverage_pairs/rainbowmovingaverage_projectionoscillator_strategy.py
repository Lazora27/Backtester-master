import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
