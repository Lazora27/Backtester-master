import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
