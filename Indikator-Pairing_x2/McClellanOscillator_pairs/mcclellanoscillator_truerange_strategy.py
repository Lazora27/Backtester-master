import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und TrueRange
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'TrueRange': 1.0
        })
    )
