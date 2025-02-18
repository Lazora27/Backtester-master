import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HullMovingAverage': 1.0
        })
    )
