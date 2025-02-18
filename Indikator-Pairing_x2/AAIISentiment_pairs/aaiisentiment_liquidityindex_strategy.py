import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'LiquidityIndex': 1.0
        })
    )
