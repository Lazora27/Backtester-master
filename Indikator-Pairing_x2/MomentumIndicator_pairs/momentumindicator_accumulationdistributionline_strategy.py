import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
