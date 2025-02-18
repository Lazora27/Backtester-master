import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
