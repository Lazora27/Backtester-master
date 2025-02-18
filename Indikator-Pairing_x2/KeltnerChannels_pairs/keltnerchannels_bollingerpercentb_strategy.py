import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'BollingerPercentB': 1.0
        })
    )
