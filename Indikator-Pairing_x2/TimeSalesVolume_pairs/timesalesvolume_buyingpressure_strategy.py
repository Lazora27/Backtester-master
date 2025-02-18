import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'BuyingPressure': 1.0
        })
    )
