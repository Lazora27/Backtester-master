import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ModifiedATR': 1.0
        })
    )
