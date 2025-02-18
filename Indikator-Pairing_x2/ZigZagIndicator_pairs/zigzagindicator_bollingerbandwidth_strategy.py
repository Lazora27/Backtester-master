import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
