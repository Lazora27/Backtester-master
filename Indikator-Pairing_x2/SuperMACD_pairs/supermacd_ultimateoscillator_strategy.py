import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'UltimateOscillator': 1.0
        })
    )
