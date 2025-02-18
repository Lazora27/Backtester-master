import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
