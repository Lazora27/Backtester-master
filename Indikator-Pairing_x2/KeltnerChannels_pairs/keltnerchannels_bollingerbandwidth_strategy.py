import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
