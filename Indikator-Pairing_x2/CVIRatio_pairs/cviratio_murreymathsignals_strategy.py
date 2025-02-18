import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
