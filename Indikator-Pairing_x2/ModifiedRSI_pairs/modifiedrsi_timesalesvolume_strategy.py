import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
