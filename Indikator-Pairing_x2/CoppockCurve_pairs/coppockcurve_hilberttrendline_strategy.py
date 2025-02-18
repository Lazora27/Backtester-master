import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HilbertTrendline': 1.0
        })
    )
