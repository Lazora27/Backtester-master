import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'KeltnerChannels': 1.0
        })
    )
