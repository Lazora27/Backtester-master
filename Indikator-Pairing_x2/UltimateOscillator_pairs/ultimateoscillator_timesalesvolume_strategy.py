import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
