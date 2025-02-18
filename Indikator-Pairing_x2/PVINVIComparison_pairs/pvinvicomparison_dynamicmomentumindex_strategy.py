import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
