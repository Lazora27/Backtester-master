import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_VolumeWeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und VolumeWeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'VolumeWeightedMovingAverage': 1.0
        })
    )
