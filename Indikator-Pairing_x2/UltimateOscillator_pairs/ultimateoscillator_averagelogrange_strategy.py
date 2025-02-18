import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'AverageLogRange': 1.0
        })
    )
