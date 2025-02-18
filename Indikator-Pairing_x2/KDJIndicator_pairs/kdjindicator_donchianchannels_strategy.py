import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'DonchianChannels': 1.0
        })
    )
