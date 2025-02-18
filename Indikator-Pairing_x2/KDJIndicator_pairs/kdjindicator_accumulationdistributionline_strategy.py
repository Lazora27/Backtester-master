import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
