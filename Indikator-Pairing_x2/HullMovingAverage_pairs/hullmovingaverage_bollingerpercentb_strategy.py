import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'BollingerPercentB': 1.0
        })
    )
