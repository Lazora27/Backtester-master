import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
