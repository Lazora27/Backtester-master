import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
