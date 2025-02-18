import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
