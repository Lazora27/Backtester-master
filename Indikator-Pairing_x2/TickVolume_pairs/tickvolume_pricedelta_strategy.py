import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und PriceDelta
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'PriceDelta': 1.0
        })
    )
