import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
