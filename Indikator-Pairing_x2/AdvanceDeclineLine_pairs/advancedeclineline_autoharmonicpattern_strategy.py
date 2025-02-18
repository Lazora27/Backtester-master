import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
