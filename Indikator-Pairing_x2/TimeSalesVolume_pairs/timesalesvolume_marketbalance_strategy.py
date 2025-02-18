import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'MarketBalance': 1.0
        })
    )
