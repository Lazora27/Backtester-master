import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MovingAverage
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MovingAverage': 1.0
        })
    )
