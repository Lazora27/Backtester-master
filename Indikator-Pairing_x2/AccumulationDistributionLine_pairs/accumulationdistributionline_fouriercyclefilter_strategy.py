import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
