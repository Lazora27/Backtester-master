import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
