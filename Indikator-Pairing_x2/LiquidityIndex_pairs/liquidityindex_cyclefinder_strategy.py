import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
