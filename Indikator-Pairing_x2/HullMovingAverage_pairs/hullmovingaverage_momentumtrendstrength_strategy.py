import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
