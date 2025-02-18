import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
