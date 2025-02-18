import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'WeeklyCycle': 1.0
        })
    )
