import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
