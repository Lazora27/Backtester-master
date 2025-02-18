import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
