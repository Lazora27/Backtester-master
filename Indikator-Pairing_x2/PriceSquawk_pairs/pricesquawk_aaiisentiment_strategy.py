import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AAIISentiment': 1.0
        })
    )
