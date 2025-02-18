import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'PriceSquawk': 1.0
        })
    )
