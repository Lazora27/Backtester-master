import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
