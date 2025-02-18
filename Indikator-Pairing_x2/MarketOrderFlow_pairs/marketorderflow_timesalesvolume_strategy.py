import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
