import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
