import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'CoppockCurve': 1.0
        })
    )
