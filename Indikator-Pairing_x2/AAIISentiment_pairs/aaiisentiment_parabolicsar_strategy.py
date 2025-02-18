import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'ParabolicSAR': 1.0
        })
    )
