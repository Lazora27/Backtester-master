import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'EhlersDecycler': 1.0
        })
    )
