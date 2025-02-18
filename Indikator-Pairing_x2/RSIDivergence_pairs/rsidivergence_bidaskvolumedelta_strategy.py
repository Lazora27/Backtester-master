import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
