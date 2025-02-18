import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'BuyingPressure': 1.0
        })
    )
