import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'DonchianVolatility': 1.0
        })
    )
