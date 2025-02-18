import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
