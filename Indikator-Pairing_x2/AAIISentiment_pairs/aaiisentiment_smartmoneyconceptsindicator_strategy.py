import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_SmartMoneyConceptsIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und SmartMoneyConceptsIndicator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'SmartMoneyConceptsIndicator': 1.0
        })
    )
