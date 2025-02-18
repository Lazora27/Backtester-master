import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AAIISentiment': 1.0
        })
    )
