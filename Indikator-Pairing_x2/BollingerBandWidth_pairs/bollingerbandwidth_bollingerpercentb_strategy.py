import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'BollingerPercentB': 1.0
        })
    )
