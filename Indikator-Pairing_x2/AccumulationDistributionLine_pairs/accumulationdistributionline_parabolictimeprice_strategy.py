import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
