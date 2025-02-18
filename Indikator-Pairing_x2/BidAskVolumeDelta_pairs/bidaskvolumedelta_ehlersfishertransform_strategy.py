import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
