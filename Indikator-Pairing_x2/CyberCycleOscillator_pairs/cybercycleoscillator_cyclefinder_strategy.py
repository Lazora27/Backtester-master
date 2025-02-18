import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
