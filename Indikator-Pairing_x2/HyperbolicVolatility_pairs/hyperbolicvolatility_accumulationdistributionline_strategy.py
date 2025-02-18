import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
