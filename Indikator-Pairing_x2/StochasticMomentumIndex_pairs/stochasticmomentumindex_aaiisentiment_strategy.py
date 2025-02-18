import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
