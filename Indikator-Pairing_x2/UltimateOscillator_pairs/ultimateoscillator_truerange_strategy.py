import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und TrueRange
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'TrueRange': 1.0
        })
    )
