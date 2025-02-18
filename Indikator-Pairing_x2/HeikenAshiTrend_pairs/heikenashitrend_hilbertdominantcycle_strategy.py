import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
