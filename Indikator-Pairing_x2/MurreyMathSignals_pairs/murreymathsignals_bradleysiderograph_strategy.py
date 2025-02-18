import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'BradleySiderograph': 1.0
        })
    )
