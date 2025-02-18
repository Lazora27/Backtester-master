import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
