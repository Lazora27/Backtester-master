import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
