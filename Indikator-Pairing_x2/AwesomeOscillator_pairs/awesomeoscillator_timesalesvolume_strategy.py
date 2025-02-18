import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
