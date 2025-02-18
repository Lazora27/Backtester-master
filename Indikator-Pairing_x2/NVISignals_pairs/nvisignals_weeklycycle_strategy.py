import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'WeeklyCycle': 1.0
        })
    )
