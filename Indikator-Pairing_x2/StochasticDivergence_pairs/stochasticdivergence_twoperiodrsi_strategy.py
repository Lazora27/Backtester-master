import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
