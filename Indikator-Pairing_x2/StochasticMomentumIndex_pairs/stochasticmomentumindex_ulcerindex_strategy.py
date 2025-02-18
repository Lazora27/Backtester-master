import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'UlcerIndex': 1.0
        })
    )
