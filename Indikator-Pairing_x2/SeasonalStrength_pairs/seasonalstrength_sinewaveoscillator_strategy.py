import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
