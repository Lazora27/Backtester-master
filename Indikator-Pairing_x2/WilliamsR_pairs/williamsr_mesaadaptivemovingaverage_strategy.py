import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MESAAdaptiveMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MESAAdaptiveMovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MESAAdaptiveMovingAverage': 1.0
        })
    )
