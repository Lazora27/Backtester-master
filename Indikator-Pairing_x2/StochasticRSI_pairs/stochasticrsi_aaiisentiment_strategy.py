import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'AAIISentiment': 1.0
        })
    )
