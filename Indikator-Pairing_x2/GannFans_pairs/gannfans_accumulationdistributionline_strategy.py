import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
