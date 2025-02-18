import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und CyberCycle
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'CyberCycle': 1.0
        })
    )
