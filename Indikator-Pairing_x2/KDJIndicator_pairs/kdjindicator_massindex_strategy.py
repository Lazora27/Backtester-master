import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MassIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MassIndex': 1.0
        })
    )
