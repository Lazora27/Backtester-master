import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
