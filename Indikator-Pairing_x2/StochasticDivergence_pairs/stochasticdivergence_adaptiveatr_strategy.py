import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AdaptiveATR': 1.0
        })
    )
