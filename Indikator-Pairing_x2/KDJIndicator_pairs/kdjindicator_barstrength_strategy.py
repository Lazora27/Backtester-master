import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
