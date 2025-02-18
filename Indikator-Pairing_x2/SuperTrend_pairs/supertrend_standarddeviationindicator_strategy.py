import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
