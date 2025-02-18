import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
