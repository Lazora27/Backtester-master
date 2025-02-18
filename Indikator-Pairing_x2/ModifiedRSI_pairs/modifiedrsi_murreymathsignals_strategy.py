import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
