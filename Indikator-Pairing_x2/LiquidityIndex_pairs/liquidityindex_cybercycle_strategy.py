import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
