import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'GannSquareReversal': 1.0
        })
    )
