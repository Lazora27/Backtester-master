import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
