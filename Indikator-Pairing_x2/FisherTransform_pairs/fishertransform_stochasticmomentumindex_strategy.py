import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
