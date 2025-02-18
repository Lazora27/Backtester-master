import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'UltimateOscillator': 1.0
        })
    )
