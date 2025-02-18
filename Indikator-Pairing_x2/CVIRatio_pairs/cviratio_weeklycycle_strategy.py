import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'WeeklyCycle': 1.0
        })
    )
