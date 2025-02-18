import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'ProjectionBands': 1.0
        })
    )
