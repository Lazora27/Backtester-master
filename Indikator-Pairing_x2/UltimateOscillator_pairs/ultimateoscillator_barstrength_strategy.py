import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und BarStrength
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'BarStrength': 1.0
        })
    )
