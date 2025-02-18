import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
