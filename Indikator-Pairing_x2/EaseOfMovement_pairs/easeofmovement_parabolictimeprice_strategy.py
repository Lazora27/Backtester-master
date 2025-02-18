import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
