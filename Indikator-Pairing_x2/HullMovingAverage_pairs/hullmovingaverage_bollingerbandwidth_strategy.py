import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
