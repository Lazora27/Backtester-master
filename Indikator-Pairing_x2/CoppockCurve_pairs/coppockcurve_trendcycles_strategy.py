import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'TrendCycles': 1.0
        })
    )
