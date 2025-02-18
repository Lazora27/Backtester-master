import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
