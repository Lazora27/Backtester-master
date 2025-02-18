import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
