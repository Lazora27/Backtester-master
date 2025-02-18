import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'TRIXIndicator': 1.0
        })
    )
