import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
