import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'LiquidityIndex': 1.0
        })
    )
