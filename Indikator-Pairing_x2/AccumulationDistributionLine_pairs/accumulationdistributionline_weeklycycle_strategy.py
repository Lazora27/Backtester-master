import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'WeeklyCycle': 1.0
        })
    )
