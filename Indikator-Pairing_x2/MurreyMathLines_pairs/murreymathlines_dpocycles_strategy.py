import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'DPOCycles': 1.0
        })
    )
