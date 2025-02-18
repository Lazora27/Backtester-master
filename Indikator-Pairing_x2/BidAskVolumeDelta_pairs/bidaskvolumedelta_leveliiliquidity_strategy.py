import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
