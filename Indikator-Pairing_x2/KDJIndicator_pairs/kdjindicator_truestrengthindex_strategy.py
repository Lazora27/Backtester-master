import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
