import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
