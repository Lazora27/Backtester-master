import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'CoppockCurve': 1.0
        })
    )
