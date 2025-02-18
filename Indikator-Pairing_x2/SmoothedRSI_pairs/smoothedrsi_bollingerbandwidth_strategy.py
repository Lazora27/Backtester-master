import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
