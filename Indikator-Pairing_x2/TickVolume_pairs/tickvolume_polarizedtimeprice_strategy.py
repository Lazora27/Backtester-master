import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
