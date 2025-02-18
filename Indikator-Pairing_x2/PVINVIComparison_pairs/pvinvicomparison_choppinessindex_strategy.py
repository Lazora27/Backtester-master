import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
