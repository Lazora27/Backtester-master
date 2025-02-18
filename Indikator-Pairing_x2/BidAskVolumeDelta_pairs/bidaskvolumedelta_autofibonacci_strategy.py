import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'AutoFibonacci': 1.0
        })
    )
