import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'CenterOfGravity': 1.0
        })
    )
