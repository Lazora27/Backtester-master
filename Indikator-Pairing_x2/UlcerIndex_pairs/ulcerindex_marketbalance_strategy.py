import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
