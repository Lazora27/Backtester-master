import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
