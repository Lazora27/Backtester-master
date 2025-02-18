import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
