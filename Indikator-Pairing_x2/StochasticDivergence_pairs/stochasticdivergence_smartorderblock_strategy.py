import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_SmartOrderBlock_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und SmartOrderBlock
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'SmartOrderBlock': 1.0
        })
    )
