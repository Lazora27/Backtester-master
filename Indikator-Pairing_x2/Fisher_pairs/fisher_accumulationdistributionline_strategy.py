import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
