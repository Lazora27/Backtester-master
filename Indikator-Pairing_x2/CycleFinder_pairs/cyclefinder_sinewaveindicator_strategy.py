import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
