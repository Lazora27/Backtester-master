import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und TrueRange
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'TrueRange': 1.0
        })
    )
