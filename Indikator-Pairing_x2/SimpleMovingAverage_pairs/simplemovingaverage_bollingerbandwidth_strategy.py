import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
