import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
