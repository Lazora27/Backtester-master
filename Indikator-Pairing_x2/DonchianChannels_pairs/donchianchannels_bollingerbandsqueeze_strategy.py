import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
