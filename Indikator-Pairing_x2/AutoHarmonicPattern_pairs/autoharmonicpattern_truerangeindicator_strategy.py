import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
