import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und SuperTrend
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'SuperTrend': 1.0
        })
    )
