import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MurreyMathLines': 1.0
        })
    )
