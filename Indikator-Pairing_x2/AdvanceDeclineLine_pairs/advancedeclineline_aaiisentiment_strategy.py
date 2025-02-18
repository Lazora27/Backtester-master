import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'AAIISentiment': 1.0
        })
    )
