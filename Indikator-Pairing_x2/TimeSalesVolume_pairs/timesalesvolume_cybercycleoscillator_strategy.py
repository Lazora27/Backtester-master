import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
