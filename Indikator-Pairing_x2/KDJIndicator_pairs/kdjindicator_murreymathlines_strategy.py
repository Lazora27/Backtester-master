import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MurreyMathLines': 1.0
        })
    )
