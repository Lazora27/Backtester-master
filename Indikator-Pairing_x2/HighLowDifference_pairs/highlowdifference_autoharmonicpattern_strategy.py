import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
