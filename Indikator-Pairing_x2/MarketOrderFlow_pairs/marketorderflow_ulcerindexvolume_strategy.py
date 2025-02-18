import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
