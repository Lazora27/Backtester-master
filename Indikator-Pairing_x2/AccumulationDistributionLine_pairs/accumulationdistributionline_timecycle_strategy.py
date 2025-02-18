import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'TimeCycle': 1.0
        })
    )
