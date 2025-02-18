import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'KeltnerChannels': 1.0
        })
    )
