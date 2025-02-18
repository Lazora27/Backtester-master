import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
