import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und GannAngles
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'GannAngles': 1.0
        })
    )
