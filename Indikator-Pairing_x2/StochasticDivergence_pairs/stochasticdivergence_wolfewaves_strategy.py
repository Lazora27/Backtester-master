import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'WolfeWaves': 1.0
        })
    )
