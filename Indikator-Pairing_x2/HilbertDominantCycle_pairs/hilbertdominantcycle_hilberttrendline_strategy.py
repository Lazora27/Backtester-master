import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'HilbertTrendline': 1.0
        })
    )
