import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
