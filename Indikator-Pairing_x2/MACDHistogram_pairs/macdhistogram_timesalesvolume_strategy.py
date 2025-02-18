import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
