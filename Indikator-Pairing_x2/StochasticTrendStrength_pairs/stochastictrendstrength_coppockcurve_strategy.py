import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'CoppockCurve': 1.0
        })
    )
