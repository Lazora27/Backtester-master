import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'CoppockCurve': 1.0
        })
    )
