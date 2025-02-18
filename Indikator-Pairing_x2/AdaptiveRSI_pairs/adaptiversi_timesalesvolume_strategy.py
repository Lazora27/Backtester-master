import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
