import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HullMovingAverage': 1.0
        })
    )
