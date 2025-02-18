import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und DPOCycles
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'DPOCycles': 1.0
        })
    )
