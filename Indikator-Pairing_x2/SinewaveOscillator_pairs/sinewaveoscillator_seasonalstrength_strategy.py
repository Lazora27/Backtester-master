import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SinewaveOscillator_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SinewaveOscillator und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'SinewaveOscillator': {
                'class': SinewaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SinewaveOscillator'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'SinewaveOscillator': 1.0,
            'SeasonalStrength': 1.0
        })
    )
