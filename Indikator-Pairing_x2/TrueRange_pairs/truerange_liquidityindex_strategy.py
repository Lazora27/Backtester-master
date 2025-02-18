import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'LiquidityIndex': 1.0
        })
    )
