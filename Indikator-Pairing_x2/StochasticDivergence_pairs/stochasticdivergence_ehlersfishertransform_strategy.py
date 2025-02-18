import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
