import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
