import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
