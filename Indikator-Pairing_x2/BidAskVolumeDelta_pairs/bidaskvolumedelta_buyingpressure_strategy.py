import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'BuyingPressure': 1.0
        })
    )
