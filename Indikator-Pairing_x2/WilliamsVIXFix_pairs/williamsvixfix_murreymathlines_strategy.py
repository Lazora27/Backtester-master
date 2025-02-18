import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MurreyMathLines': 1.0
        })
    )
