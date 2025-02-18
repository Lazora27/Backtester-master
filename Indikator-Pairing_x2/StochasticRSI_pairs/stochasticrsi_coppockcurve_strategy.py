import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'CoppockCurve': 1.0
        })
    )
