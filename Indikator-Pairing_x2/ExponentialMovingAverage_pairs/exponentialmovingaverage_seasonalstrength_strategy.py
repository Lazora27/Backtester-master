import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'SeasonalStrength': 1.0
        })
    )
