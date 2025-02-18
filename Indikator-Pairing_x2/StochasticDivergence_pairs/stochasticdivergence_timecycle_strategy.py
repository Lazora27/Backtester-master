import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TimeCycle
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TimeCycle': 1.0
        })
    )
