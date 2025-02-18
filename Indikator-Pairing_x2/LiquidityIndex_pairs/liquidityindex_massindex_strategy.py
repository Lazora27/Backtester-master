import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'MassIndex': 1.0
        })
    )
