import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
