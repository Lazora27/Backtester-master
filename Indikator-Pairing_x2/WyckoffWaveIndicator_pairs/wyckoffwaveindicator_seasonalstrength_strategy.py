import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffWaveIndicator_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffWaveIndicator und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'WyckoffWaveIndicator': 1.0,
            'SeasonalStrength': 1.0
        })
    )
