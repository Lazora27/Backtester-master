import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
