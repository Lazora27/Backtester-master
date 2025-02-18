import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MomentumIndicator': 1.0
        })
    )
