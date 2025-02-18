import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'DonchianChannels': 1.0
        })
    )
