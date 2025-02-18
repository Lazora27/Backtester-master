import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
