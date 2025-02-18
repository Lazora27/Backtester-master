import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'TRIXIndicator': 1.0
        })
    )
