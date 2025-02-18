import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
