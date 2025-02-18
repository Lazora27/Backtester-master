import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VerticalHorizontalFilter_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VerticalHorizontalFilter und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'VerticalHorizontalFilter': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
