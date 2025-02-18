import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
