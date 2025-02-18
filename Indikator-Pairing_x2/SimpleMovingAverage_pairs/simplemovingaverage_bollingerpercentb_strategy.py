import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'BollingerPercentB': 1.0
        })
    )
