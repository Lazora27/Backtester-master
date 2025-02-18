import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
