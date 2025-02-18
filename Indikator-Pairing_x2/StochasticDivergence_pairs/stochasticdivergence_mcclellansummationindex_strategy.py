import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
