import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'DonchianChannels': 1.0
        })
    )
