import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
