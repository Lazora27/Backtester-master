import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'CoppockCurve': 1.0
        })
    )
