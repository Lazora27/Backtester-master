import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CCITurbo
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CCITurbo': 1.0
        })
    )
