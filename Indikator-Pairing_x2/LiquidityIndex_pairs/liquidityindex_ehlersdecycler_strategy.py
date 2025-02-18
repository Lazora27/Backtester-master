import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
