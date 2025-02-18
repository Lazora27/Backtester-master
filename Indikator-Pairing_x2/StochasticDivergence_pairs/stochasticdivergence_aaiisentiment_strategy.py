import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AAIISentiment': 1.0
        })
    )
