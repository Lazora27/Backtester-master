import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und TimeCycle
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'TimeCycle': 1.0
        })
    )
