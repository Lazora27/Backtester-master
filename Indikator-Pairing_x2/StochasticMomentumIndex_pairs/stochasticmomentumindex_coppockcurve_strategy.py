import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
