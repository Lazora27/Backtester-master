import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'ExtensionProjections': 1.0
        })
    )
