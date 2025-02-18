import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'VolatilityIndex': 1.0
        })
    )
