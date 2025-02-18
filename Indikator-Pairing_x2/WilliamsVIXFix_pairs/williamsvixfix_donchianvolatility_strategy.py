import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'DonchianVolatility': 1.0
        })
    )
