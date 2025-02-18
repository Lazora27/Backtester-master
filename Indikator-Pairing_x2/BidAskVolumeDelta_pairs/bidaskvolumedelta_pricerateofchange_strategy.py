import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
