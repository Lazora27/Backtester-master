import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
