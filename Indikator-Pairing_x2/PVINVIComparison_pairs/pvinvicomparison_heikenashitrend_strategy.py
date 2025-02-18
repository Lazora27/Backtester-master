import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
