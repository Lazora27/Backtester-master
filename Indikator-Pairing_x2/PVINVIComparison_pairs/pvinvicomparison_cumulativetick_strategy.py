import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'CumulativeTick': 1.0
        })
    )
