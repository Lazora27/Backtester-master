import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
