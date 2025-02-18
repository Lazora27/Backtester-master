import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedMovingAverage_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedMovingAverage und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'VolumeWeightedMovingAverage': 1.0,
            'FlowOfFunds': 1.0
        })
    )
