import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
