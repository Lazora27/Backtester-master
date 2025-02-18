import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'CCITurbo': 1.0
        })
    )
