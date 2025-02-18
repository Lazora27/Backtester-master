import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'StochasticRSI': 1.0
        })
    )
