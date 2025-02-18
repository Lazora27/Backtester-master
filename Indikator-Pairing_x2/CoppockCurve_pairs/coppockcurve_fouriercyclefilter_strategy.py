import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
