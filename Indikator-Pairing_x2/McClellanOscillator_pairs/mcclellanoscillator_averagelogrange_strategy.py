import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'AverageLogRange': 1.0
        })
    )
