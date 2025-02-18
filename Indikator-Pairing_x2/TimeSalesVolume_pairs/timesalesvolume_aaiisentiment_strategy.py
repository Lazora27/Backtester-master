import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AAIISentiment': 1.0
        })
    )
