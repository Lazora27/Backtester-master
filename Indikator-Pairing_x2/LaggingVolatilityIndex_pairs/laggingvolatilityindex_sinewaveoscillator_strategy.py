import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LaggingVolatilityIndex_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LaggingVolatilityIndex und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'LaggingVolatilityIndex': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
