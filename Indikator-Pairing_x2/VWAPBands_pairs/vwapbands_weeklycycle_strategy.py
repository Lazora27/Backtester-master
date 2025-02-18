import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'WeeklyCycle': 1.0
        })
    )
