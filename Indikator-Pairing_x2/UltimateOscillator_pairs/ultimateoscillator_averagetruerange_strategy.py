import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
