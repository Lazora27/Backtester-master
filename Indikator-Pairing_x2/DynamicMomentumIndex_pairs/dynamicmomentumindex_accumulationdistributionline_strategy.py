import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
