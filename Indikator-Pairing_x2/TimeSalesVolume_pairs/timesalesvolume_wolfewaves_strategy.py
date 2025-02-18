import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'WolfeWaves': 1.0
        })
    )
