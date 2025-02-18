import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'LiquidityIndex': 1.0
        })
    )
