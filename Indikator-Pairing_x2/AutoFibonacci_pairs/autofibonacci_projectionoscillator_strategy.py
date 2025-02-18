import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
