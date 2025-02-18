import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_NormalizedVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und NormalizedVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'NormalizedVolatilityIndex': 1.0
        })
    )
