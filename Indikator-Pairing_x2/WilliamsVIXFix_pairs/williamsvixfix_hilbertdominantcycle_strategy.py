import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
