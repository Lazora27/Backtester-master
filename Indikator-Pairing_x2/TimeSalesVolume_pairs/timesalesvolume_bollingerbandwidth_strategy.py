import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
