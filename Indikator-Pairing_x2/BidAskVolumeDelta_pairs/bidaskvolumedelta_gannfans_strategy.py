import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und GannFans
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'GannFans': 1.0
        })
    )
