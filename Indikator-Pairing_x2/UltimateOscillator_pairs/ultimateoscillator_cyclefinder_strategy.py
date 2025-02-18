import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
