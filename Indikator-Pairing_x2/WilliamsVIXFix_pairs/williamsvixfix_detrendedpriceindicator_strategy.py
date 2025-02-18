import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_DetrendedPriceIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und DetrendedPriceIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'DetrendedPriceIndicator': 1.0
        })
    )
