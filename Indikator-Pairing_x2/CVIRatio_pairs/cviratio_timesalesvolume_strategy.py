import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
