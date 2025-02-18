import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'AroonIndicator': 1.0
        })
    )
