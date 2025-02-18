import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'AverageLogRange': 1.0
        })
    )
