import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'DonchianChannels': 1.0
        })
    )
