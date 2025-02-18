import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'KeltnerChannels': 1.0
        })
    )
