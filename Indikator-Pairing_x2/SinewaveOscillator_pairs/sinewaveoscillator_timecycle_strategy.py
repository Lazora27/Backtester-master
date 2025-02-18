import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SineWaveOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
