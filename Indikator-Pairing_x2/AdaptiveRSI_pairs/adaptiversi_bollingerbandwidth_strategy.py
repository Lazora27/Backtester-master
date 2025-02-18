import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
