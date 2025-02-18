import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'CoppockCurve': 1.0
        })
    )
