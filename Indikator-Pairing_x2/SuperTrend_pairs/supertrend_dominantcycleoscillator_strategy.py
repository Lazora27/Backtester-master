import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
