import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'EaseOfMovement': 1.0
        })
    )
