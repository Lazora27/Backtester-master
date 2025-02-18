import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
