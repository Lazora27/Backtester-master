import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'LiquidityIndex': 1.0
        })
    )
