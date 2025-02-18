import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
