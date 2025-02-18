import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PriceDelta
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PriceDelta': 1.0
        })
    )
