import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BollingerPercentB': 1.0
        })
    )
