import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
