import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
