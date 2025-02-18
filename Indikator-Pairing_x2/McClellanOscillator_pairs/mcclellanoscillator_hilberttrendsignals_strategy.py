import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
