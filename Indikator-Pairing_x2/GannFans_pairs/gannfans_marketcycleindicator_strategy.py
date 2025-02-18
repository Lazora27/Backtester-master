import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
