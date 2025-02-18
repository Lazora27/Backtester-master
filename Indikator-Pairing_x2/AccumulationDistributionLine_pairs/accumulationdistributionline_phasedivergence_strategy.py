import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'PhaseDivergence': 1.0
        })
    )
