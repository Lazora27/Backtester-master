import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'BuyingPressure': 1.0
        })
    )
