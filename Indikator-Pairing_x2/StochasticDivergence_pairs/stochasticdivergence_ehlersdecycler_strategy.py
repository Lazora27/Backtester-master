import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'EhlersDecycler': 1.0
        })
    )
