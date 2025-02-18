import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
