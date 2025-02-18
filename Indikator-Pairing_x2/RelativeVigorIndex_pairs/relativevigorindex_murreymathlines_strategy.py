import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
