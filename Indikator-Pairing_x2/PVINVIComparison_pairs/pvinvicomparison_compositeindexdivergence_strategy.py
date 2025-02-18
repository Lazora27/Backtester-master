import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
