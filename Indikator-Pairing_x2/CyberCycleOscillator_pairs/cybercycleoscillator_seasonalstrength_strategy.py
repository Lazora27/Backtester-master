import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'SeasonalStrength': 1.0
        })
    )
