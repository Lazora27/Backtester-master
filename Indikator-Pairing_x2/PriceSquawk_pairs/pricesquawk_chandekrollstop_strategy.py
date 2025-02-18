import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
