import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'LiquidityIndex': 1.0
        })
    )
