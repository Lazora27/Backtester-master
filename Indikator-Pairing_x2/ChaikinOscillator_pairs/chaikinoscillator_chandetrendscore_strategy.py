import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
