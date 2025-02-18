import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und MassIndex
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'MassIndex': 1.0
        })
    )
