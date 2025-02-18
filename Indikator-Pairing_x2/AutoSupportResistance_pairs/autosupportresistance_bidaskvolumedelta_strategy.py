import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
