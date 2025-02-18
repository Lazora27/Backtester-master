import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
