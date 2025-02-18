import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'BollingerPercentB': 1.0
        })
    )
