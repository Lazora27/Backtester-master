import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
