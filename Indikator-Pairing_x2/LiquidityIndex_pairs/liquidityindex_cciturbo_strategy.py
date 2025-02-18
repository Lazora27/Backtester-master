import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
