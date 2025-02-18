import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
