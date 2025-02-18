import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
