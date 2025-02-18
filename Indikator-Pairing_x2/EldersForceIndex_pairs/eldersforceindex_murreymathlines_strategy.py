import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
