import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MurreyMathLines': 1.0
        })
    )
