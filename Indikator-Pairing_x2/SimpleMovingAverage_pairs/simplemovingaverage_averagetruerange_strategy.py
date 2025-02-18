import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'AverageTrueRange': 1.0
        })
    )
