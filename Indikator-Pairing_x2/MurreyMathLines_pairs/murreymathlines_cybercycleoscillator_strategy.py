import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
