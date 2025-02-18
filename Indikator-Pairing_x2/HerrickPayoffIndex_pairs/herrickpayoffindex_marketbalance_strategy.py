import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
