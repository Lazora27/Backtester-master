import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'UltimateOscillator': 1.0
        })
    )
