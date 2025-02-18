import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
