import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'SmoothedRSI': 1.0
        })
    )
