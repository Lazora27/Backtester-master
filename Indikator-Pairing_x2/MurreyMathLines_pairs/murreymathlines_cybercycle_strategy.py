import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'CyberCycle': 1.0
        })
    )
