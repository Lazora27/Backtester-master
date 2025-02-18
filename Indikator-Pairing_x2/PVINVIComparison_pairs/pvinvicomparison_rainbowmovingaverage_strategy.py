import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
