import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FisherTransform
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FisherTransform': 1.0
        })
    )
