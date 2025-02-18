import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
