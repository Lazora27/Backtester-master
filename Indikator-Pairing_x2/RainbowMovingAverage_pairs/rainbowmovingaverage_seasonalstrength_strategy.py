import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'SeasonalStrength': 1.0
        })
    )
