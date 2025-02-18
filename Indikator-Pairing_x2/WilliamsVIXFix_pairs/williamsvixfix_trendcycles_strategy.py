import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und TrendCycles
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'TrendCycles': 1.0
        })
    )
