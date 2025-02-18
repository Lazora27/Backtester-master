import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'BollingerBands': 1.0
        })
    )
