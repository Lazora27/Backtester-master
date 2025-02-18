import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
