import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_WyckoffWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und WyckoffWaveIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'WyckoffWaveIndicator': 1.0
        })
    )
