import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
