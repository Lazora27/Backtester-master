import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
