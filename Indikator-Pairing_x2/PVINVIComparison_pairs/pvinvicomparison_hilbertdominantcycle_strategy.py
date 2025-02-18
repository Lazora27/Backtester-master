import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
