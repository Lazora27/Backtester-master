import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CoppockCurve': 1.0
        })
    )
