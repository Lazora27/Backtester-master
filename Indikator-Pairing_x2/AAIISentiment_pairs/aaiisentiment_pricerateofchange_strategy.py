import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
