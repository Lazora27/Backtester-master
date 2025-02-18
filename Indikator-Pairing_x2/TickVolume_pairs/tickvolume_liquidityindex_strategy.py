import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'LiquidityIndex': 1.0
        })
    )
