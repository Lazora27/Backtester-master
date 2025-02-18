import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
