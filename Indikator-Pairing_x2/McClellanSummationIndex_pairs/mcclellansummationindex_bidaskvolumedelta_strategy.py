import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
