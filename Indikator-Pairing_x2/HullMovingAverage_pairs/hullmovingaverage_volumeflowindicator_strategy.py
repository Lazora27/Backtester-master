import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
