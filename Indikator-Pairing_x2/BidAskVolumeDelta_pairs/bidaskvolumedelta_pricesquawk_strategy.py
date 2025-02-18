import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'PriceSquawk': 1.0
        })
    )
