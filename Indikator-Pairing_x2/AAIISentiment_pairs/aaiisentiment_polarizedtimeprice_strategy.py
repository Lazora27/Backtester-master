import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
