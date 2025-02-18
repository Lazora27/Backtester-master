import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'LiquidityIndex': 1.0
        })
    )
