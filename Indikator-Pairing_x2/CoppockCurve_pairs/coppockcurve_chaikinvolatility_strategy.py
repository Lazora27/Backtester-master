import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
