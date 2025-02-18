import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'TrendCycles': 1.0
        })
    )
