import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
