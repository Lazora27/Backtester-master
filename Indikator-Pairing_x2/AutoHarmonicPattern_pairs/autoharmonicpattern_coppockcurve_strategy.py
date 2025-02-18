import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'CoppockCurve': 1.0
        })
    )
