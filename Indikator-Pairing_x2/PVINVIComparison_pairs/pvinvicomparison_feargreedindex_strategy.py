import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FearGreedIndex': 1.0
        })
    )
