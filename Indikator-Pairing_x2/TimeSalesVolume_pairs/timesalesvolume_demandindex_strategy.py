import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und DemandIndex
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'DemandIndex': 1.0
        })
    )
