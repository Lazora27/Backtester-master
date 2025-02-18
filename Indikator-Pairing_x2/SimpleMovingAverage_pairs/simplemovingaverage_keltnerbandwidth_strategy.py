import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
