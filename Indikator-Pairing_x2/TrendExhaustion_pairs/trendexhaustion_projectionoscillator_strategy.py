import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
