import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
