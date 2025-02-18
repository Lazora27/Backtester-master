import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'WeeklyCycle': 1.0
        })
    )
