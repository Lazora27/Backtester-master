import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
