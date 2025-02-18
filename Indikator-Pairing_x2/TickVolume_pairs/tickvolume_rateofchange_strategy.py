import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und RateOfChange
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'RateOfChange': 1.0
        })
    )
