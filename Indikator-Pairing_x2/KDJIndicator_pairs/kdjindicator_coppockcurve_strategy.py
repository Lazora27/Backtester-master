import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'CoppockCurve': 1.0
        })
    )
