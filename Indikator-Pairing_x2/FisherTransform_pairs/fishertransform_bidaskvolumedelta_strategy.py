import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
