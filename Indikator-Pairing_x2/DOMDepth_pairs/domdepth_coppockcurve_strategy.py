import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'CoppockCurve': 1.0
        })
    )
