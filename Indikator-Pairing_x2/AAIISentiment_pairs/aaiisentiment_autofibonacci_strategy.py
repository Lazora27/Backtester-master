import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AutoFibonacci': 1.0
        })
    )
