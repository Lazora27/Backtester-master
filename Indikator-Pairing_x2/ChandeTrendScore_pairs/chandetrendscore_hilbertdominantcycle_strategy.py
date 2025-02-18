import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
