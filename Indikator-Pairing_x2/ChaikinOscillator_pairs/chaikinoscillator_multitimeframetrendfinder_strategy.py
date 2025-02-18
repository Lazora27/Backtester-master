import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MultiTimeframeTrendFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MultiTimeframeTrendFinder
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MultiTimeframeTrendFinder': 1.0
        })
    )
