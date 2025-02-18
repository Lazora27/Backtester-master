import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
