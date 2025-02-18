import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
