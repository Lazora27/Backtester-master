import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
