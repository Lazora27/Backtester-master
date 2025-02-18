import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
