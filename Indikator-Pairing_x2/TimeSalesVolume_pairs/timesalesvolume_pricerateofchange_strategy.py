import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
