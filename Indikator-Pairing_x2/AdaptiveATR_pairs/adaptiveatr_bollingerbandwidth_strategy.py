import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
