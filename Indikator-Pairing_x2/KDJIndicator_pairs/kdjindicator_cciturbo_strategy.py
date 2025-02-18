import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
