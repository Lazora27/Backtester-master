import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
