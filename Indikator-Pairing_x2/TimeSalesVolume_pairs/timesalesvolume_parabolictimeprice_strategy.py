import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
