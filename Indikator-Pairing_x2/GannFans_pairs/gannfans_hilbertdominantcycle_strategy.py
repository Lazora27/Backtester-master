import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
