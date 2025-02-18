import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'LiquidityIndex': 1.0
        })
    )
