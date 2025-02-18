import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
