import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
