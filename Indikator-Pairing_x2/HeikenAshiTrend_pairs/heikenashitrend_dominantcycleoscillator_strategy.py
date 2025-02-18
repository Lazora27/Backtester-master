import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
