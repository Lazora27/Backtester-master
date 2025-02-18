import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
