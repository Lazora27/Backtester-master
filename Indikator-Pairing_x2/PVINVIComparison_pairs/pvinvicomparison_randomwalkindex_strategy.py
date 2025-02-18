import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
