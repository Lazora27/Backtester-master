import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
