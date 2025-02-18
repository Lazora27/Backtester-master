import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'AAIISentiment': 1.0
        })
    )
