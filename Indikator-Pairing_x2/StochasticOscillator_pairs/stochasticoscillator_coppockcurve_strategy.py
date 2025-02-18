import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'CoppockCurve': 1.0
        })
    )
