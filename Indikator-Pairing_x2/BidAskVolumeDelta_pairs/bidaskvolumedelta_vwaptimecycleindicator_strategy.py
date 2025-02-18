import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_VWAPTimeCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und VWAPTimeCycleIndicator
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'VWAPTimeCycleIndicator': 1.0
        })
    )
