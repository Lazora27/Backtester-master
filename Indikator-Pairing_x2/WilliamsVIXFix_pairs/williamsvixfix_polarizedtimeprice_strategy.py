import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
