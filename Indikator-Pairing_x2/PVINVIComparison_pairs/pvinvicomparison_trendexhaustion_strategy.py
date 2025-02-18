import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TrendExhaustion': 1.0
        })
    )
