import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und TrueRange
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'TrueRange': 1.0
        })
    )
