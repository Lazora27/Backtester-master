import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AAIISentiment': 1.0
        })
    )
