import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'OpenInterest': 1.0
        })
    )
