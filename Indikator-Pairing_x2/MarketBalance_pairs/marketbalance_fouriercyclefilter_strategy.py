import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
