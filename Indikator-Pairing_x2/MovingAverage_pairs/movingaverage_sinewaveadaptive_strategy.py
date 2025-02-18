import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
