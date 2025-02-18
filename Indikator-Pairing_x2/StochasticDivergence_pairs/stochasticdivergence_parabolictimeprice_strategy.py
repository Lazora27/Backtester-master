import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
