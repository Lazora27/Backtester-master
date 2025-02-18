import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BuyingPressure': 1.0
        })
    )
