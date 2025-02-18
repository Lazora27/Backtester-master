import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
