import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'DPOCycles': 1.0
        })
    )
