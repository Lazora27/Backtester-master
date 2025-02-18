import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
