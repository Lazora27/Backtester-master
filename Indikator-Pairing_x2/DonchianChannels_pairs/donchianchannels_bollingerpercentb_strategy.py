import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'BollingerPercentB': 1.0
        })
    )
