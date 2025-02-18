import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
