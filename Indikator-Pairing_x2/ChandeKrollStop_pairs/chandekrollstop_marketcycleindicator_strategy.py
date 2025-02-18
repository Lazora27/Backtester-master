import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
